from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.utils.translation import ugettext, ugettext_lazy as _

import re


def lowercase_email(email):
    """
    Normalize the address by lowercasing the domain part of the email
    address.
    """
    email = email or ''
    try:
        email_name, domain_part = email.strip().rsplit('@', 1)
    except ValueError:
        pass
    else:
        email = '@'.join([email_name.lower(), domain_part.lower()])
    return email


class SignupForm(forms.ModelForm):
    username = forms.CharField(
        label='用户名', required=True,
        error_messages={'required': '请填写你的用户名', 'max_length': '最多只能输入15个字符', 'min_length': '至少输入3个字符'}, max_length=15,
        min_length=3, widget=forms.TextInput(attrs={'placeholder': '3~15位字母/数字/汉字'}))
    email = forms.EmailField(error_messages={'required': '请填写你的email', 'invalid': 'email格式不正确'},
                             label='邮箱', required=True,
                             widget=forms.EmailInput(attrs={'placeholder': '填写正确的email以便激活你的账户'}))
    password = forms.CharField(
        error_messages={'required': '请输入密码', 'max_length': '最多只能输入20个字符', 'min_length': '至少输入6个字符'},
        label='密码', required=True, max_length=20, widget=forms.PasswordInput(attrs={'placeholder': '长度在6~20个字符以内'}))
    confirm_password = forms.CharField(
        error_messages={'required': '请输入密码', 'max_length': '最多只能输入20个字符', 'min_length': '至少输入6个字符'},
        label='确认密码', required=True, max_length=20, min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder': '长度在6~20个字符以内'}))

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password",)

    def clean_email(self):
        UserModel = get_user_model()
        email = self.cleaned_data["email"]
        lower_email = lowercase_email(email)
        try:
            UserModel._default_manager.get(email=lower_email)
        except UserModel.DoesNotExist:
            return lower_email
        raise forms.ValidationError("有人已经注册了这个email地址")

    def clean_confirm_password(self):
        # cleaned_data=super(SignupForm,self).clean()
        password = self.cleaned_data.get("password", False)
        confirm_password = self.cleaned_data["confirm_password"]
        if not (password == confirm_password):
            raise forms.ValidationError("确认密码和密码不一致")
        return confirm_password

    def clean_username(self):
        UserModel = get_user_model()
        username = self.cleaned_data["username"]
        # 过滤用户名敏感词的注册用户
        n = re.sub('[^\u4e00-\u9fa5a-zA-Z]', '', username)

        mgc = ['admin', 'k']

        if n in mgc:
            raise forms.ValidationError(" 换一个")

        try:
            UserModel._default_manager.get(username=username)

        except UserModel.DoesNotExist:
            return username
        raise forms.ValidationError("有人已经注册了这个用户名")

class Reset_emailForm(forms.Form):
    email = forms.EmailField(error_messages={'required': '请填写你的email', 'invalid': 'email格式不正确'},
                             label='邮箱', required=True,
                             widget=forms.EmailInput(attrs={'placeholder': '请输入你的注册邮箱'}))

    def clean_email(self):
        UserModel = get_user_model()
        email = self.cleaned_data["email"]
        lower_email = lowercase_email(email)
        try:
            UserModel._default_manager.get(email=lower_email)
        except UserModel.DoesNotExist:
            raise forms.ValidationError("还没有人注册这个邮箱")
        return lower_email

class Change_passwordForm(forms.Form):
    password = forms.CharField(
        error_messages={'required': '请输入密码', 'max_length': '最多只能输入20个字符', 'min_length': '至少输入6个字符'},
        label='密码', required=True, max_length=20, widget=forms.PasswordInput(attrs={'placeholder': '长度在6~20个字符以内'}))
    confirm_password = forms.CharField(
        error_messages={'required': '请输入密码', 'max_length': '最多只能输入20个字符', 'min_length': '至少输入6个字符'},
        label='确认密码', required=True, max_length=20, min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder': '长度在6~20个字符以内'}))
    def clean_confirm_password(self):
        # cleaned_data=super(SignupForm,self).clean()
        password = self.cleaned_data.get("password", False)
        confirm_password = self.cleaned_data["confirm_password"]
        if not (password == confirm_password):
            raise forms.ValidationError("确认密码和密码不一致")
        return confirm_password




class LoginForm(forms.Form):
    username = forms.CharField(
        label='用户名', required=False)
    password = forms.CharField(
        label='密码', required=False, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        UserModel = get_user_model()
        username = cleaned_data.get("username")
        username = username.strip()
        password = cleaned_data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                return cleaned_data
            else:
                raise forms.ValidationError("该账号被禁止登录")

        if not username or not password:
            raise forms.ValidationError("用户名/密码不能为空")

        else:
            raise forms.ValidationError("密码和用户名不匹配")


class Completion(forms.ModelForm):
    stu_calss = forms.CharField()
    tele_num = forms.IntegerField()

    class Meta:
        model = get_user_model()
        fields = ( "stu_calss", "tele_num",)



