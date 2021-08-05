import MySQLdb
import hashlib
import django
import cgi
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def test_api(request):
    return django.http.JsonResponse({
        "result":0,
        "msg":"执行成功"
    })

@csrf_exempt
def login(request):
    if request.method != 'GET':

        return django.http.JsonResponse({
        "result":-100,
        "msg":"Parameter Wrong"
    })
    username, password = request.GET["username"], request.GET["password"]
    db = MySQLdb.connect("w3.zhangxinran.net", "root", "mysql#1357924680aA", "UserInformation", charset='utf8' )
    cursor = db.cursor()
    cursor.execute("select User_Password_Hash from UserInformation where User_Name = %s;", (username,))
    data = cursor.fetchone()
    if not data:
        db.close()
        return django.http.JsonResponse({
        "result":-200,
        "msg":"User Not Exist"
    })
    elif str(data[0]) == str(hashlib.sha512(password.encode('utf-8')).hexdigest()).upper():
        return django.http.JsonResponse({
        "result":0,
        "msg":"Login Success",
        "accessToken": str(hashlib.sha512(username.encode('utf-8')).hexdigest()).upper()
    })
    else:
        db.close()
        return django.http.JsonResponse({
        "result":-300,
        "msg":"Password Error"
    })


@csrf_exempt
def register(request):
    if request.method != 'GET':
        return django.http.JsonResponse({
        "result":-100,
        "msg":"Parameter Wrong"
    })
    username, password = request.GET["username"], request.GET["password"]
    db = MySQLdb.connect("w3.zhangxinran.net", "root", "mysql#1357924680aA", "UserInformation", charset='utf8' )
    cursor = db.cursor()
    cursor.execute("SELECT count( * ) FROM UserInformation WHERE `User_Name` = %s;", (username,))
    data = cursor.fetchone()
    hash = str(hashlib.sha512(password.encode('utf-8')).hexdigest()).upper()
    if data[0] != 0:
        db.close()
        return django.http.JsonResponse({
        "result":-400,
        "msg":"User Already Exists"
    })
    else:
        print(hash)
        sql = "INSERT INTO UserInformation (User_Name, User_Password_Hash) VALUES (%s, %s)"
        val = (username, hash)
        cursor.execute(sql , val)
        db.commit()        
        data = cursor.fetchone()
        db.close()
        return django.http.JsonResponse({
        "result":0,
        "msg":"Login Success",
        "accessToken":str(hashlib.sha512(username.encode('utf-8')).hexdigest()).upper()
    })


@csrf_exempt
def uploadText(request):
    if request.method != 'POST':
        return django.http.JsonResponse({
        "result":-100,
        "msg":"Parameter Wrong"
    })
    accessToken, fileName, fileContent = request.POST.get('accessToken',0), request.POST.get('fileName',0), request.POST.get('fileContent',0)
    db = MySQLdb.connect("w3.zhangxinran.net", "root", "mysql#1357924680aA", "UserInformation", charset='utf8' )
    cursor = db.cursor()
    cursor.execute("SELECT count( * ) FROM Articles WHERE `Aritcle_Name` = %s;", (fileName,))
    data = cursor.fetchone()
    if data[0] != 0:
        db.close()
        return django.http.JsonResponse({
        "result":-400,
        "msg":"File Already Exists"
    })
    else:
        print(hash)
        sql = "INSERT INTO Articles (Aritcle_Name, Article_Owner, Article_Content) VALUES (%s, %s, %s)"
        val = (str(fileName), str(accessToken), str(fileContent))
        cursor.execute(sql , val)
        db.commit()        
        data = cursor.fetchone()
        db.close()
        return django.http.JsonResponse({
        "result":0,
        "msg":"Add Success",
        "accessToken":accessToken
    })

@csrf_exempt
def getText(request):
    if request.method != 'GET':
        return django.http.JsonResponse({
        "result":-100,
        "msg":"Parameter Wrong"
    })
    filename= request.GET["filename"]
    db = MySQLdb.connect("w3.zhangxinran.net", "root", "mysql#1357924680aA", "UserInformation", charset='utf8' )
    cursor = db.cursor()
    cursor.execute("SELECT count( * ) FROM Articles WHERE `Aritcle_Name` = %s;", (filename,))
    data = cursor.fetchone()
    if data[0] != 1:
        db.close()
        return django.http.JsonResponse({
        "result":-400,
        "msg":"File Do Not Exists"
    })
    else:
        print(hash)
        cursor.execute("select Article_Content from Articles where Aritcle_Name = %s;", (filename,))
        data = cursor.fetchone()
        db.close()
        return django.http.JsonResponse({
        "result":0,
        "msg":"Get Success",
        "text": data[0]
    })


print(django.VERSION)    
