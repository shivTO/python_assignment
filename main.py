import boto3 
from io import StringIO
import falcon
import pandas as pd
s3 = boto3.resource('s3',
aws_access_key_id= access_id,
        aws_secret_access_key= key,
)

bucket = s3.Bucket('irisbucket111')

class Resource:
    def on_get(self,req,res):
        res.status = falcon.HTTP_200
        res.body="service is running"
    def on_post(self,req,res):
        data=req.media
        print(data)
        
        for obj in bucket.objects.all():
            key = obj.key
            body = obj.get()['Body'].read().decode("utf-8")
        csvStringIO = StringIO(body)

        df = pd.read_csv(csvStringIO, sep=",", header=None)
        print(df)
        new= [data['pl'],data['pw'],data['sl'],data['sw'],data['cl']]
        df = df.append(pd.Series(new, index=df.columns[:len(new)]), ignore_index=True)
        res.status = falcon.HTTP_200
        res.body="added data successfully"
        csv_buffer = StringIO()
        df.to_csv(csv_buffer)
        s3.Object('irisbucket111', 'irisfolder/iris.data').put(Body=csv_buffer.getvalue())


app=falcon.API()
resapi=Resource()
app.add_route('/api', resapi)