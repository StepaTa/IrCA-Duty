from idm.objects import dp, MySignalEvent

eng = u"~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"

rus = u"ё!\"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"

fonts = {
    '1': u"~!@#&#38;%^&𝕢𝕨𝕖𝕣𝕥𝕪𝕦𝕚𝕠𝕡[]𝕒𝕤𝕕𝕗𝕘𝕙𝕛𝕜𝕝;'𝕫𝕩𝕔𝕧𝕓𝕟𝕞,./ℚ𝕎𝔼ℝ𝕋𝕐𝕌𝕀𝕆ℙ{}𝔸𝕊𝔻𝔽𝔾ℍ𝕁𝕂𝕃:\"|ℤ𝕏ℂ𝕍𝔹ℕ𝕄<>?",
	'2': u"~!@#&#38;%^&𝚚𝚠𝚎𝚛𝚝𝚢𝚞𝚒𝚘𝚙[]𝚊𝚜𝚍𝚏𝚐𝚑𝚓𝚔𝚕;'𝚣𝚡𝚌𝚟𝚋𝚗𝚖,./𝚀𝚆𝙴𝚁𝚃𝚈𝚄𝙸𝙾𝙿{}𝙰𝚂𝙳𝙵𝙶𝙷𝙹𝙺𝙻:\"|𝚉𝚇𝙲𝚅𝙱𝙽𝙺<>?",
    '3': u"~!@#&#38;%^&𝓆𝓌ℯ𝓇𝓉𝓎𝓊𝒾ℴ𝓅[]𝒶𝓈𝒹𝒻ℊ𝒽𝒿𝓀𝓁;'𝓏𝓍𝒸𝓋𝒷𝓃𝓂,./𝒬𝒲ℰℛ𝒯𝒴𝒰ℐ𝒪𝒫{}𝒜𝒮𝒟ℱ𝒢ℋ𝒥𝒦ℒ:\"|𝒵𝒳𝒞𝒱ℬ𝒩ℳ<>?",
    '4': u"~!@#&#38;%^&𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹[]𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵;'𝔃𝔁𝓬𝓿𝓫𝓷𝓶,./𝓠𝓦𝓔𝓡𝓣𝓨𝓤𝓘𝓞𝓟{}𝓐𝓢𝓓𝓕𝓖𝓗𝓙𝓚𝓛:\"|𝓩𝓧𝓒𝓥𝓑𝓝𝓜<>?",
	'5': u"~¡@#&#38;%^&bʍǝɹʇʎnᴉod[]ɐspɟƃɥɾʞl;'zxɔʌquɯ,./bʍǝɹʇʎnᴉod{}ɐspɟƃɥɾʞl:\"|zxɔʌquɯ<>¿",
	'6': u"~!@#&#38;%^&ǫᴡᴇʀᴛʏᴜɪᴏᴘ[]ᴀsᴅғɢʜᴊᴋʟ;'ᴢxᴄᴠʙɴᴍ,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?",
	'7': u"~!@#&#38;%^&ᑫᗯᗴᖇTYᑌIOᑭ[]ᗩՏᗪᖴᘜᕼᒍKᒪ;'ᘔ᙭ᑕᐯᗷᑎᗰ,./ᑫᗯᗴᖇTYᑌIOᑭ{}ᗩՏᗪᖴᘜᕼᒍKᒪ:\"|ᘔ᙭ᑕᐯᗷᑎᗰ<>?",
	'8': u"~!@#&#38;%^&𝐪𝐰𝐞𝐫𝐭𝐲𝐮𝐢𝐨𝐩[]𝐚𝐬𝐝𝐟𝐠𝐡𝐣𝐤𝐥;'𝐳𝐱𝐜𝐯𝐛𝐧𝐦,./𝐐𝐖𝐄𝐑𝐓𝐘𝐔𝐈𝐎𝐏{}𝐀𝐒𝐃𝐅𝐆𝐇𝐉𝐊𝐋:\"|𝐙𝐗𝐂𝐕𝐁𝐍𝐌<>?",
	'9': u"~!@#&#38;%^&𝑞𝑤𝑒𝑟𝑡𝑦𝑢𝑖𝑜𝑝[]𝑎𝑠𝑑𝑓𝑔ℎ𝑗𝑘𝑙;'𝑧𝑥𝑐𝑣𝑏𝑛𝑚,./𝑄𝑊𝐸𝑅𝑇𝑌𝑈𝐼𝑂𝑃{}𝐴𝑆𝐷𝐹𝐺𝐻𝐽𝐾𝐿:\"|𝑍𝑋𝐶𝑉𝐵𝑁𝑀<>?",
	'10': u"~!@#&#38;%^&𝒒𝒘𝒆𝒓𝒕𝒚𝒖𝒊𝒐𝒑[]𝒂𝒔𝒅𝒇𝒈𝒉𝒋𝒌𝒍;'𝒛𝒙𝒄𝒗𝒃𝒏𝒎,./𝑸𝑾𝑬𝑹𝑻𝒀𝑼𝑰𝑶𝑷{}𝑨𝑺𝑫𝑭𝑮𝑯𝑱𝑲𝑳:\"|𝒁𝑿𝑪𝑽𝑩𝑵𝑴<>?",
	'11': u"~!@#&#38;%^&ⓆⓌⒺⓇⓉⓎⓊⒾⓄⓅ[]ⒶⓈⒹⒻⒼⒽⒿⓀⓁ;'ⓏⓍⒸⓋⒷⓃⓂ,./ⓆⓌⒺⓇⓉⓎⓊⒾⓄⓅ{}ⒶⓈⒹⒻⒼⒽⒿⓀⓁ:\"|ⓏⓍⒸⓋⒷⓃⓂ<>?",
	'12': u"~!@#&#38;%^&🅠🅦🅔🅡🅣🅨🅤🅘🅞🅟[]🅐🅢🅓🅕🅖🅗🅙🅚🅛;'🅩🅧🅒🅥🅑🅝🅜,./🅠🅦🅔🅡🅣🅨🅤🅘🅞🅟{}🅐🅢🅓🅕🅖🅗🅙🅚🅛:\"|🅩🅧🅒🅥🅑🅝🅜<>?",
	'13': u"~!@#&#38;%^&🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿[]🄰🅂🄳🄵🄶🄷🄹🄺🄻;'🅉🅇🄲🅅🄱🄽🄼,./🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿{}🄰🅂🄳🄵🄶🄷🄹🄺🄻:\"|🅉🅇🄲🅅🄱🄽🄼<>?",
	'14': u"~!@#&#38;%^&𝔮𝔴𝔢𝔯𝔱𝔶𝔲𝔦𝔬𝔭[]𝔞𝔰𝔡𝔣𝔤𝔥𝔧𝔨𝔩;'𝔷𝔵𝔠𝔳𝔟𝔫𝔪,./𝔔𝔚𝔈ℜ𝔗𝔜𝔘ℑ𝔒𝔓{}𝔄𝔖𝔇𝔉𝔊ℌ𝔍𝔎𝔏:\"|ℨ𝔛ℭ𝔙𝔅𝔑𝔐<>?",
	'15': u"~!@#&#38;%^&𝖖𝖜𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕[]𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑;'𝖟𝖝𝖈𝖛𝖇𝖓𝖒,./𝕼𝖂𝕰𝕽𝕿𝖄𝖀𝕴𝕺𝕻{}𝕬𝕾𝕯𝕱𝕲𝕳𝕵𝕶𝕷:\"|𝖅𝖃𝕮𝖁𝕭𝕹𝕸<>?"

    }

translit = u'ё|!|"|№|;|%|:|?|y|ts|u|k|e|n|g|sh|sch|z|kh||f|y|v|a|p|r|o|l|d|zh|e|ya|ch|s|m|i|t||b|yu|.|Y|TS|U|K|E|N|G|SH|SCH|Z|KH||F|Y|B|A|P|R|O|L|D|ZH|E|/|YA|CH|S|M|I|T||B|YU|'
translit = dict(zip(rus, translit.split('|')))


@dp.longpoll_event_register('конв', '-конв')
@dp.my_signal_event_register('конв', '-конв')
def conv_text(event: MySignalEvent) -> str:
    trans_table = dict(zip(eng, rus)) if event.command == 'конв' else dict(zip(rus, eng))
    s = ''
    if event.args:
        s = " ".join(event.args)
    if event.payload:
        s = s + '\n' + event.payload
    if event.reply_message:
        s = s + '\n' + event.reply_message['text']
    if event.msg['fwd_messages']:
        for i in event.msg['fwd_messages']:
            s += '\n\n' + i['text']

    if s == '':
        event.msg_op(2, 'Нет данных 🤦')
        return "ok"

    message = u''.join([trans_table.get(c, c) for c in s])
    event.msg_op(2, message, keep_forward_messages=1)
    return "ok"


@dp.longpoll_event_register('шрифты')
@dp.my_signal_event_register('шрифты')
def fonts_list(event: MySignalEvent) -> str:
    event.msg_op(2, """
    1. 𝕠𝕦𝕥𝕝𝕚𝕟𝕖 (outline)
    2. 𝚝𝚢𝚙𝚎𝚠𝚛𝚒𝚝𝚎𝚛 (typewriter)
    3. 𝓈𝒸𝓇𝒾𝓅𝓉 (script)
    4. 𝓼𝓬𝓻𝓲𝓹𝓽_𝓫𝓸𝓵𝓭 (script_bold)
    5. uʍop_ǝpᴉsdn (upside_down)
    6. ᴛɪɴʏ_ᴄᴀᴘs (tiny_caps)
    7. ᑕOᗰIᑕ (comic)
    8. 𝐬𝐞𝐫𝐢𝐟_𝐛 (serif_b)
    9. 𝑠𝑒𝑟𝑖𝑓_𝑖 (serif_i)
    10. 𝒔𝒆𝒓𝒊𝒇_𝒃𝒊 (serif_bi)
    11. ⒸⒾⓇⒸⓁⒺⓈ (circles)
    12. 🅒🅘🅡🅒🅛🅔🅢_🅑 (circles_b)
    13. 🅂🅀🅄🄰🅁🄴🅂 (squares)
    14. 𝔤𝔬𝔱𝔥𝔦𝔠 (gothic)
    15. 𝖌𝖔𝖙𝖍𝖎𝖈_𝖇 (gothic_b)""".replace('    ', ''))
    return "ok"


@dp.longpoll_event_register('шрифт')
@dp.my_signal_event_register('шрифт')
def fonts_convert(event: MySignalEvent) -> str:
    dest = False
    if event.args:
        if event.args[0] in fonts.keys():
            message = f'{" ".join(event.args[1:])}\n{event.payload}'
            dest = fonts[event.args[0]]
            s = ''.join(translit.get(c, c) for c in message)
            msg = u''.join(dict(zip(eng, dest)).get(c, c) for c in s)
            if event.args[0] == '5':
                msg = msg[::-1]
    if not dest:
        msg = """Просмотр списка шрифтов - .с шрифты
        \nКоманда для конвертации:\n.с шрифт [номер]\n[текст]"""
    event.msg_op(2, msg, keep_forward_messages=1)
    return "ok"
