# Uncertify
Uncertify is a tool written in Python that allows to bypass, in an automated way, the most common mechanisms used in Android apps to implement certificate pinning. In addition to that Uncertify can also bypass other OkHttp configuration settings such as:

- [Certificate pinning](https://square.github.io/okhttp/4.x/okhttp/okhttp3/-certificate-pinner/)
- [Interceptors](https://square.github.io/okhttp/interceptors/)
- [Dns](https://square.github.io/okhttp/3.x/okhttp/okhttp3/OkHttpClient.Builder.html#dns-okhttp3.Dns-)
- [Follow redirects](https://square.github.io/okhttp/4.x/okhttp/okhttp3/-ok-http-client/-builder/follow-redirects/)

Uncertify also has an option to enables log traces with information about every HTTP request when the app uses OkHttp.


### ❱ Dependencies
--------------------------------------
- [Python](https://www.python.org/download/releases/3.0/)
- [Apktool](https://ibotpeaches.github.io/Apktool/) 2.4.0 or newer recommended
- [jarsigner](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jarsigner.html)
- [zipalign](https://developer.android.com/studio/command-line/zipalign)

Apktool, jarsigner and zipalign must be added to PATH

### ❱ Python dependencies
--------------------------------------
- [Click](https://click.palletsprojects.com/en/7.x/). It can be installed trough `pip3 install click`

### ❱ How to use it
--------------------------------------
```
git clone https://github.com/felHR85/Uncertify.git
cd Uncertify
python3 uncertify.py PATH_TO_APK --pinning
```
The provided apk will be decompiled, modified and rebuild again with name app-uncertify.apk

### ❱ Options
--------------------------------------
- --pinning: Bypass certificate pinning
- --interceptors: Bypass OkHttp interceptors
- --dns: Bypass OkHttp DNS configuration. It will use the default one
- --follow: Bypass OkHttp follow redirects and follow ssl redirects
- --logs: Enables OkHttp logs. It can be shown using adb shell logcat | grep OkHttp (or Android Studio logcat tab)

### ❱ Docker
--------------------------------------
TODO

### ❱ License
--------------------------------------
MIT License

Copyright (c) 2020 Felipe Herranz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.