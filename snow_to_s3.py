from stat import SF_ARCHIVED
import boto3
import snowflake.connector as sf

s3 = boto3.client('s3')

def lambda_handler(event, context):

    # connect to snowflake
    ctx = sf.connect(
        user='',
        password='',
        account=''
    )

    # create a cursor object so we can make queries
    cs = ctx.cursor()

    # execute a query to the updating database
    cs.execute('select * from "DEV"."SSAVAS_EXPORT"."PRODUCT_DATA"')

    # get the info from the query into a variable
    product_table = cs.fetchall()


    '''
    
    STILL NEED TO PLAY WITH S3
    
    # send the query info into an s3 file
    response = s3.put_object(
        Body=(bytes(json.dumps(product_table).encode('UTF-8'))),
        Bucket='___',
        Key='___'
    )
    '''
    return {
        'statusCode': 200,
        'body': product_table
    }
    
