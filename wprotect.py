import zipfile
import os
import shutil


def isProtect(solists):
    solists = ",".join(list(solists))
    if solists.find('libtup.so') != -1 or solists.find('libshell') != -1:
        print("腾讯乐固加固")
    elif solists.find('librsprotect.so') != -1:
        print("瑞星")
    elif solists.find('libapssec.so') != -1:
        print("盛大")
    elif solists.find('libx3g.so') != -1:
        print("顶象科技")
    elif solists.find('libkwscmm.so') != -1 or solists.find('libkwscr.so') != -1 or solists.find('libkwslinker.so')!= -1:
        print("几维安全加固")
    elif solists.find('libAPKProtect.so') != -1:
        print("APKProtect")
    elif solists.find('libnesec.so') != -1:
        print("网易易盾加固")
    elif solists.find('libtosprotection.armeabi.so') != -1 or solists.find('libtosprotection.armeabi-v7a.so') != -1 or solists.find('libtosprotection.x86.so') != -1:
        print("腾讯御安全加固")
    elif solists.find('libsgmain.so') != -1 or solists.find('libsgsecuritybody.so') != -1 or solists.find('libmobisec.so') != -1:
        print("阿里聚安全加固")
    elif solists.find('libbaiduprotect.so') != -1:
        print("百度加固")
    elif solists.find('libnqshield.so') != -1:
        print("网秦加固")
    elif solists.find('libegis.so') != -1 or solists.find('libNSaferOnly.so') != -1:
        print("通付盾加固")
    elif solists.find('libprotectClass.so') != -1 or solists.find('libjiagu.so') != -1 or solists.find('libjiagu_art.so') != -1 or solists.find('libjiagu_x86.so') != -1:
        print("360加固")
    elif solists.find('libDexHelper.so') != -1 or solists.find('libDexHelper-x86.so') != -1:
        print("梆梆加固企业版")
    elif solists.find('libsecexe.so') != -1 or solists.find('libsecmain.so') != -1 or solists.find('libSecShell.so') != -1:
        print("梆梆加固")
    elif solists.find('libexec.so') != -1 or solists.find('libexecmain.so') != -1:
        print("爱加密加固")
    elif solists.find('libedog.so') != -1:
        print('娜迦加固企业版')
    elif solists.find('libchaosvmp.so') != -1 or solists.find('libddog.so') != -1 or solists.find('libfdog.so') != -1:
        print("娜迦加固")




if __name__ == '__main__':

    print("input absPath:")
    apkPath = input()
    solists = []
    if(os.path.isfile(apkPath) == False):
        print("目录不存在")
        exit()
    shutil.copy(apkPath,"src.apk")
    srcPath = os.path.abspath("src.apk")
    print(srcPath)
    portion = os.path.splitext(srcPath)
    newname = ''
    if portion[1] == ".apk":
        newname = portion[0] + ".zip"
        os.rename(srcPath,newname)
        print(newname)

    if newname.endswith(".zip"):
        print("hello")
        z = zipfile.ZipFile(newname,'r')

        for filename in z.namelist():
            if filename.endswith(".so"):
                filename = os.path.basename(filename)
                solists.append(filename)

        print(solists)

        isProtect(solists)
        z.close()

    if os.path.isfile('src.zip'):

        os.remove('src.zip')

