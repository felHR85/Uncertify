# Method keys
add_interceptor = 'addInterceptor'
add_network_interceptor = 'addNetworkInterceptor'
authenticator = 'authenticator'
cache = 'cache'
call_timeout_1 = 'callTimeOut1'
call_timeout_2 = 'callTimeOut2'
certificate_pinner = 'certificatePinner'
connection_pool = 'connection_pool'
connection_specs = 'connection_specs'
connect_timeout_1 = 'connectTimeout1'
connect_timeout_2 = 'connectTimeout2'
cookie_jar = "cookieJar"
dispatcher = "dispatcher"
dns = "dns"
event_listener = 'eventListener'
event_listener_factory = 'eventListenerFactory'
follow_redirects = 'followRedirects'
follow_ssl_redirects = 'followSslRedirects'
hostname_verifier = 'hostnameVerifier'
interceptors = 'interceptors'
pingInterval_1 = 'ping_interval1'
pingInterval_2 = 'ping_interval2'
protocols = 'protocols'
proxy = 'proxy'
proxy_authenticator = 'proxyAuthenticator'
proxy_selector = 'proxySelector'
read_timeout_1 = 'read_timeout_1'
read_timeout_2 = 'read_timeout_2'
retry_on_connection_failure = 'retryOnConnectionFailure'
socket_factory = 'socketFactory'
ssl_socket_factory_1 = 'sslSocketFactory1'
ssl_socket_factory_2 = 'sslSocketFactory2'
write_timeout_1 = 'writeTimeout1'
write_timeout_2 = 'writeTimeout2'


# Method declaration dictionary
okhttp_methods = {
    add_interceptor : '.method public addInterceptor(Lokhttp3/Interceptor;)Lokhttp3/OkHttpClient$Builder',
    add_network_interceptor : '.method public addNetworkInterceptor(Lokhttp3/Interceptor;)Lokhttp3/OkHttpClient$Builder',
    authenticator : '.method public authenticator(Lokhttp3/Authenticator;)Lokhttp3/OkHttpClient$Builder',
    cache : '.method public cache(Lokhttp3/Cache;)Lokhttp3/OkHttpClient$Builder',
    call_timeout_1 : '.method public callTimeout(JLjava/util/concurrent/TimeUnit;)Lokhttp3/OkHttpClient$Builder',
    call_timeout_2 : '.method public callTimeout(Ljava/time/Duration;)Lokhttp3/OkHttpClient$Builder;',
    certificate_pinner : '.method public certificatePinner(Lokhttp3/CertificatePinner;)Lokhttp3/OkHttpClient$Builder;',
    connection_pool : '.method public connectionPool(Lokhttp3/ConnectionPool;)Lokhttp3/OkHttpClient$Builder',
    connection_specs : '.method public connectionSpecs(Ljava/util/List;)Lokhttp3/OkHttpClient$Builder',
    connect_timeout_1 : '.method public connectTimeout(JLjava/util/concurrent/TimeUnit;)Lokhttp3/OkHttpClient$Builder',
    connect_timeout_2 : '.method public connectTimeout(Ljava/time/Duration;)Lokhttp3/OkHttpClient$Builder',
    cookie_jar : '.method public cookieJar(Lokhttp3/CookieJar;)Lokhttp3/OkHttpClient$Builder',
    dispatcher : '.method public dispatcher(Lokhttp3/Dispatcher;)Lokhttp3/OkHttpClient$Builder',
    dns : '.method public dns(Lokhttp3/Dns;)Lokhttp3/OkHttpClient$Builder',
    event_listener : '.method public eventListener(Lokhttp3/EventListener;)Lokhttp3/OkHttpClient$Builder',
    event_listener_factory : '.method public eventListenerFactory(Lokhttp3/EventListener$Factory;)Lokhttp3/OkHttpClient$Builder',
    follow_redirects : '.method public followRedirects(Z)Lokhttp3/OkHttpClient$Builder',
    follow_ssl_redirects : '.method public followSslRedirects(Z)Lokhttp3/OkHttpClient$Builder',
    hostname_verifier : '.method public hostnameVerifier(Ljavax/net/ssl/HostnameVerifier;)Lokhttp3/OkHttpClient$Builder',
    pingInterval_1 : '.method public pingInterval(JLjava/util/concurrent/TimeUnit;)Lokhttp3/OkHttpClient$Builder',
    pingInterval_2 : '.method public pingInterval(Ljava/time/Duration;)Lokhttp3/OkHttpClient$Builder',
    protocols : '.method public protocols(Ljava/util/List;)Lokhttp3/OkHttpClient$Builder',
    proxy : '.method public proxy(Ljava/net/Proxy;)Lokhttp3/OkHttpClient$Builder',
    proxy_authenticator : '.method public proxyAuthenticator(Lokhttp3/Authenticator;)Lokhttp3/OkHttpClient$Builder',
    proxy_selector : '.method public proxySelector(Ljava/net/ProxySelector;)Lokhttp3/OkHttpClient$Builder',
    read_timeout_1 : '.method public readTimeout(JLjava/util/concurrent/TimeUnit;)Lokhttp3/OkHttpClient$Builder',
    read_timeout_2 : '.method public readTimeout(Ljava/time/Duration;)Lokhttp3/OkHttpClient$Builder',
    retry_on_connection_failure : 'method public retryOnConnectionFailure(Z)Lokhttp3/OkHttpClient$Builder',
    socket_factory : '.method public socketFactory(Ljavax/net/SocketFactory;)Lokhttp3/OkHttpClient$Builder',
    ssl_socket_factory_1 : '.method public sslSocketFactory(Ljavax/net/ssl/SSLSocketFactory;)Lokhttp3/OkHttpClient$Builder',
    ssl_socket_factory_2 : '.method public sslSocketFactory(Ljavax/net/ssl/SSLSocketFactory;Ljavax/net/ssl/X509TrustManager;)Lokhttp3/OkHttpClient$Builder',
    write_timeout_1 : '.method public writeTimeout(JLjava/util/concurrent/TimeUnit;)Lokhttp3/OkHttpClient$Builder',
    write_timeout_2 : '.method public writeTimeout(Ljava/time/Duration;)Lokhttp3/OkHttpClient$Builder'
}

# End method
end_method = ".end method"

# injects
locals_declaration = "\t.locals 2\n"
param_declaration = "\t.param p1, \"parameter\"\n"
return_declaration = "\treturn-object p0\n"