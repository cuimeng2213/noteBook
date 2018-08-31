import json
import random
import datetime
from django.shortcuts import render
from django.views.generic.base import View
from Service.models import CMDBUser
from django.http import JsonResponse

#导入数据库
from Api.models import Token
from Service.models import Cpu
from Service.models import Memory
from Service.models import Service
from Service.models import Service_Cpu
from Service.models import Service_Memory

def getToken(user_id):
	temp="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	value = "".join(random.sample(temp, 8))
	t = Token()
	t.value =value
	t.time = 3600
	t.create_time = datetime.datetime.now()
	t.user_id = user_id
	t.save()
	return value

class CMDBApi(View):
	def __init__(self, **kwargs):
		View.__init__(self,**kwargs)
		self.result = {
			"status":"error",
			"data":{},
			"error":""
		}

		self.item = list(
				filter(lambda x:x.startswith("api_"),dir(self))
			)
		self.dict = CMDBApi.__dict__

	def api_login(self):
		username = self.postData.get("username")
		password = self.postData.get("password")
		#
		if username:
			try:
				user = CMDBUser.objects.get(username = username)
			except Exception as e:
				self.result["error"] = "your name is error"
			else:
				db_password = user.password
				if password == db_password:
					user_id = user.id
					token = getToken(user_id)
					self.result["status"] = "success"
					self.result["data"] = {"token":token}
				else:
					self.result["error"] = "password is error"
	def api_sendServer(self):
		#获取的客户端提交的数据
		post_server = json.loads(self.postData.get("server"))
		post_cpu = json.loads(self.postData["cpu"])
		post_memory = json.loads(self.postData["memory"])

		print("serverinfo", post_server)

		#保存服务器基础信息
		if post_server:
			server = Service()
			server.hostname = post_server.get("hostname")
			server.ip = post_server.get("ip")
			server.mac = post_server.get("mac")
			server.cpu = post_server.get("cpu")
			server.memory = post_server.get("memory")
			server.isalive = 'true'
			server.save()
		else:
			server = None

		#保存cpu信息
		#cpu 字段太多，所以一定注意接口的提交的关键字和数据库的对应
		cpu = Cpu()
		cpu.processor = post_cpu.get("processor")
		cpu.vendor_id = post_cpu.get("vendor_id")
		cpu.cpu_family = post_cpu.get("cpu_family")
		cpu.model = post_cpu.get("model")
		cpu.model_name = post_cpu.get("model_name")
		cpu.stepping = post_cpu.get("stepping")
		cpu.microcode = post_cpu.get("microcode")
		cpu.cpu_MHz = post_cpu.get("cpu_MHz")
		cpu.cache_size = post_cpu.get("cache_size")
		cpu.physical_id = post_cpu.get("physical_id")
		cpu.siblings = post_cpu.get("siblings")
		cpu.core_id = post_cpu.get("core_id")
		cpu.cpu_cores = post_cpu.get("cpu_cores")
		cpu.apicid = post_cpu.get("apicid")
		cpu.initial_apicid = post_cpu.get("initial_apicid")
		cpu.fpu = post_cpu.get("fpu")
		cpu.fpu_exception = post_cpu.get("fpu_exception")
		cpu.cpuid_level = post_cpu.get("cpuid_level")
		cpu.wp = post_cpu.get("wp")
		cpu.flags = post_cpu.get("flags")
		cpu.bogomips = post_cpu.get("bogomips")
		cpu.clflush_size = post_cpu.get("clflush_size")
		cpu.cache_alignment = post_cpu.get("cache_alignment")
		cpu.address_sizes = post_cpu.get("address_sizes")
		cpu.power_management = post_cpu.get("power_management")
		cpu.save()

		#保存内存
		memory = Memory()
		memory.MemTota = post_memory.get("MemTota")
		memory.MemFree = post_memory.get("MemFree")
		memory.MemAvailable = post_memory.get("MemAvailable")
		memory.Buffers = post_memory.get("Buffers")
		memory.Cached = post_memory.get("Cached")
		memory.SwapCached = post_memory.get("SwapCached")
		memory.Active = post_memory.get("Active")
		memory.Inactive = post_memory.get("Inactive")
		memory.Active_anon = post_memory.get("Active_anon")
		memory.Inactive_anon = post_memory.get("Inactive_anon")
		memory.Active_file = post_memory.get("Active_file")
		memory.Inactive_file = post_memory.get("Inactive_file")
		memory.Unevictable = post_memory.get("Unevictable")
		memory.Mlocked = post_memory.get("Mlocked")
		memory.SwapTotal = post_memory.get("SwapTotal")
		memory.SwapFree = post_memory.get("SwapFree")
		memory.Dirty = post_memory.get("Dirty")
		memory.Writeback = post_memory.get("Writeback")
		memory.AnonPages = post_memory.get("AnonPages")
		memory.Mapped = post_memory.get("Mapped")
		memory.Shmem = post_memory.get("Shmem")
		memory.Slab = post_memory.get("Slab")
		memory.SReclaimable = post_memory.get("SReclaimable")
		memory.SUnreclaim = post_memory.get("SUnreclaim")
		memory.KernelStack = post_memory.get("KernelStack")
		memory.PageTables = post_memory.get("PageTables")
		memory.NFS_Unstable = post_memory.get("NFS_Unstable")
		memory.Bounce = post_memory.get("Bounce")
		memory.WritebackTmp = post_memory.get("WritebackTmp")
		memory.CommitLimit = post_memory.get("CommitLimit")
		memory.Committed_AS = post_memory.get("Committed_AS")
		memory.VmallocTotal = post_memory.get("VmallocTotal")
		memory.VmallocUsed = post_memory.get("VmallocUsed")
		memory.VmallocChunk = post_memory.get("VmallocChunk")
		memory.HardwareCorrupted = post_memory.get("HardwareCorrupted")
		memory.AnonHugePages = post_memory.get("AnonHugePages")
		memory.HugePages_Total = post_memory.get("HugePages_Total")
		memory.HugePages_Free = post_memory.get("HugePages_Free")
		memory.HugePages_Rsvd = post_memory.get("HugePages_Rsvd")
		memory.HugePages_Surp = post_memory.get("HugePages_Surp")
		memory.Hugepagesize = post_memory.get("Hugepagesize")
		memory.DirectMap4k = post_memory.get("DirectMap4k")
		memory.DirectMap2M = post_memory.get("DirectMap2M")
		memory.DirectMap1G = post_memory.get("DirectMap1G")
		memory.save()
		#server对应CPU关系保存
		s_c = Service_Cpu()
		if server:
			s_c.service_id = server.id
		s_c.cpu_id = cpu.id
		s_c.save()
		#server对象memory关系保存
		s_m = Service_Memory()
		if server:
			s_m.service_id = server.id
		s_m.Memory_id = memory.id
		s_m.save()
		self.result["status"] = "success"
		self.result["data"] = "your server is saved"
	def get(self,request):
		item = self.dict
		return render(request, "get_page.html", locals())

	def post(self, request):
		if request.method == "POST" and request.POST:
			data = request.POST
			ty = data.get("type")
			dt = data.get("data")
			tk = data.get("token")
			self.postData = json.loads(dt.replace("\'","\""))
			print(self.postData)
			ty_name = "api_"+ty
			if ty and ty_name in self.item:
				# try:
				self.dict[ty_name](self)
				# except Exception as e:
				# 	print('error is',e)
			else:
				self.result["error"] = "we have no method named %s" % ty
		return JsonResponse(self.result)
