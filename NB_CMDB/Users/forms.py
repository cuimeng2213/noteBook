from django import forms

class CMDBUserForm(forms.Form):
    username = forms.CharField(max_length = 32,verbose_name = "用户账号")
    password = forms.CharField(max_length = 32,verbose_name = "用户密码")
    nickname = forms.CharField(max_length = 32,verbose_name = "用户姓名")
    phone = forms.CharField(max_length = 32,verbose_name = "用户手机号")
    email = forms.EmailField(verbose_name = "用户邮箱")
    photo = forms.ImageField(verbose_name = "用户头像",upload_to = "images")
    service = forms.ManyToManyField(Service) #通过这个字段创建关联
