from itertools import islice

def insertToDb(df, modelObj):
    """Utility to bulk insert data into models"""

    num = df._get_numeric_data()
    num[num < 0] = 0
    records = df.to_dict('records')
    print('Deleting all records from {} table'.format(modelObj._meta.db_table))
    modelObj.objects.all().delete()
    print('Inserting records into {} table'.format(modelObj._meta.db_table))
    countdata = 0
    while countdata < len(records):
        try:
            modelObj.objects.bulk_create(
                modelObj(**vals) for vals in records[countdata:countdata + 100]
            )
            print("{} records inserted".format(countdata))
        except Exception as e:
            print(e)
        countdata += 100
    return '{} records inserted in {}'.format(len(records), modelObj._meta.db_table)