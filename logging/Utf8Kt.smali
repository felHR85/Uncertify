.class public final Lokhttp3/logging/Utf8Kt;
.super Ljava/lang/Object;
.source "utf8.kt"


# annotations
.annotation runtime Lkotlin/Metadata;
    bv = {
        0x1,
        0x0,
        0x3
    }
    d1 = {
        "\u0000\u000c\n\u0000\n\u0002\u0010\u000b\n\u0002\u0018\u0002\n\u0000\u001a\u000c\u0010\u0000\u001a\u00020\u0001*\u00020\u0002H\u0000\u00a8\u0006\u0003"
    }
    d2 = {
        "isProbablyUtf8",
        "",
        "Lokio/Buffer;",
        "okhttp-logging-interceptor"
    }
    k = 0x2
    mv = {
        0x1,
        0x1,
        0x10
    }
.end annotation


# direct methods
.method public static final isProbablyUtf8(Lokio/Buffer;)Z
    .locals 8
    .param p0, "$this$isProbablyUtf8"    # Lokio/Buffer;
        .annotation build Lorg/jetbrains/annotations/NotNull;
        .end annotation
    .end param

    const-string v0, "$this$isProbablyUtf8"

    invoke-static {p0, v0}, Lkotlin/jvm/internal/Intrinsics;->checkParameterIsNotNull(Ljava/lang/Object;Ljava/lang/String;)V

    .line 27
    nop

    .line 28
    const/4 v0, 0x0

    :try_start_0
    new-instance v2, Lokio/Buffer;

    invoke-direct {v2}, Lokio/Buffer;-><init>()V

    .line 29
    .local v2, "prefix":Lokio/Buffer;
    invoke-virtual {p0}, Lokio/Buffer;->size()J

    move-result-wide v3

    const-wide/16 v5, 0x40

    invoke-static {v3, v4, v5, v6}, Lkotlin/ranges/RangesKt;->coerceAtMost(JJ)J

    move-result-wide v5

    .line 30
    .local v5, "byteCount":J
    const-wide/16 v3, 0x0

    move-object v1, p0

    invoke-virtual/range {v1 .. v6}, Lokio/Buffer;->copyTo(Lokio/Buffer;JJ)Lokio/Buffer;

    .line 31
    const/16 v1, 0x10

    const/4 v3, 0x0

    :goto_0
    if-ge v3, v1, :cond_2

    .line 32
    .local v3, "i":I
    invoke-virtual {v2}, Lokio/Buffer;->exhausted()Z

    move-result v4

    if-eqz v4, :cond_0

    .line 33
    goto :goto_1

    .line 35
    :cond_0
    invoke-virtual {v2}, Lokio/Buffer;->readUtf8CodePoint()I

    move-result v4

    .line 36
    .local v4, "codePoint":I
    invoke-static {v4}, Ljava/lang/Character;->isISOControl(I)Z

    move-result v7

    if-eqz v7, :cond_1

    invoke-static {v4}, Ljava/lang/Character;->isWhitespace(I)Z

    move-result v7
    :try_end_0
    .catch Ljava/io/EOFException; {:try_start_0 .. :try_end_0} :catch_0

    if-nez v7, :cond_1

    .line 37
    return v0

    .line 31
    .end local v4    # "codePoint":I
    :cond_1
    add-int/lit8 v3, v3, 0x1

    goto :goto_0

    .line 40
    .end local v3    # "i":I
    :cond_2
    :goto_1
    const/4 v0, 0x1

    return v0

    .line 41
    .end local v2    # "prefix":Lokio/Buffer;
    .end local v5    # "byteCount":J
    :catch_0
    move-exception v1

    .line 42
    .local v1, "_":Ljava/io/EOFException;
    return v0
.end method
