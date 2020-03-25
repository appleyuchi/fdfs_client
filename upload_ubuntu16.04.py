from fdfs_client.client import Fdfs_client, get_tracker_conf
tracker_path = get_tracker_conf('/etc/fdfs/client.conf')
client = Fdfs_client(tracker_path)
ret = client.upload_by_filename('1.jpg')
print(ret)