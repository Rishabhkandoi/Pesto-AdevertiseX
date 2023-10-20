# Example code for loading data into a storage system (e.g., Hadoop HDFS)

from hdfs import InsecureClient

def load_data_to_hdfs(data, hdfs_path):
    client = InsecureClient('http://hadoop-namenode:50070', user='your_user')
    with client.write(hdfs_path, overwrite=True) as writer:
        writer.write(data)

# Example usage
load_data_to_hdfs(impressions_data, '/data/impressions.json')

