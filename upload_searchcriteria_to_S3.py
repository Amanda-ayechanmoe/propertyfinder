import boto3
import pandas as pd


def search_param(filter_list):
    print(filter_list)
    l = []

    for filters in filter_list:
        d = {}
        if len(filters):
            d['filters'] = filters

        if (len(d) != 0):
            l.append(d)

    df = pd.DataFrame(l)
    print(df)
    df.to_csv('search.csv')
    upload_S3()


def upload_S3():
    # Intilize interfaces
    s3Client = boto3.client('s3')
    s3Resource = boto3.resource('s3')

    # get csv file in-memory
    with open('output.csv', 'rb') as file:
        # put_object
        response = s3Client.put_object(
            Body=file,
            Bucket='my-search-filter-buk',
            Key='search.csv',
            ContentType='text/csv'
        )

    print(response)
