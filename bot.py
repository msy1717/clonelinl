import ytdl

client = TelegramClient('mrunal', api_id, api_hash).start(bot_token=token)

@client(

    pattern="^/song",
async def download_from_youtube_(event):

    opt = event.pattern_match.group(1)

    xx = await eor(event, get_string("com_1"))

    if opt == "a":

        ytd = {

            "format": "bestaudio",

            "addmetadata": True,

            "geo-bypass": True,

            "nocheckcertificate": True,

            "outtmpl": "%(id)s.mp3",

        }

        url = event.pattern_match.group(2)

        if not url:

            return await eor(xx, "Give me a (youtube) URL to download audio from!")

        try:

            request.get(url)

        except BaseException:

            return await eor(xx, "`Give A Direct Audio Link To Download`")

    elif opt == "v":

        ytd = {

            "format": "best",

            "addmetadata": True,

            "geo-bypass": True,

            "nocheckcertificate": True,

            "outtmpl": "%(id)s.mp4",

        }

        url = event.pattern_match.group(2)

        if not url:

            return await eor(xx, "Give me a (youtube) URL to download video from!")

        try:

            request.get(url)

        except BaseException:

            return await eor(xx, "`Give A Direct Video Link To Download`")

    elif opt == "sa":

        ytd = {

            "format": "bestaudio",

            "addmetadata": True,

            "geo-bypass": True,

            "nocheckcertificate": True,

            "outtmpl": "%(id)s.mp3",

        }

        try:

            query = event.text.split(" ", 1)[1]

        except IndexError:

            return await eor(

                xx, "Give me a (youtube) search query to download audio from!"

            )

        url = get_yt_link(query)

        await eor(xx, "`Downloading audio song...`")

    elif opt == "sv":

        ytd = {

            "format": "best",

            "addmetadata": True,

            "geo-bypass": True,

            "nocheckcertificate": True,

            "outtmpl": "%(id)s.mp4",

        }

        try:

            query = event.text.split(" ", 1)[1]

        except IndexError:

            return await eor(

                xx, "Give me a (youtube) search query to download video from!"

            )

        url = get_yt_link(query)

        await eor(xx, "`Downloading video song...`")

    else:

        return

    await download_yt(xx, url, ytd)
