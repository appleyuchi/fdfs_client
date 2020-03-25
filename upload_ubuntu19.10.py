from fdfs_client.client import Fdfs_client
client = Fdfs_client('/etc/fdfs/client.conf')
ret = client.upload_by_filename('1.jpg')
print("ret=",ret)