from django import forms

class CMDBUserForm(forms.Form):
    username = forms.CharField( label='用户账号',widget = forms.TextInput(
    	attrs = {	
    				'class':'form-control',
    				'maxlength':6,
    				'minlength':2,
    				'required':'',
    			}))
    password = forms.CharField( label='用户密码', widget=forms.PasswordInput(
    	attrs = {
    		'class':'form-control',
    		'maxlength':16,
    		'minlength':8,
    		'required':''
    	}
    	))
    nickname = forms.CharField(label='用户姓名', widget = forms.TextInput(
    	attrs = {
    		'class':'form-control',
    		'required':'',
    	}
    	))
    phone = forms.CharField( label='用户电话', widget = forms.TextInput(
    	attrs={
    		'class':'form-control',
    		'required':'',
    	}))
    email = forms.EmailField(label='用户邮箱', widget=forms.EmailInput(
    	attrs={
    		'class':'form-control',
    		'required':'',
    	}))
    photo = forms.ImageField(label='用户头像')
   
