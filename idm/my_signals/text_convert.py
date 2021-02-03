from idm.objects import dp, MySignalEvent

eng = u"~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"

rus = u"ё!\"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"

fonts = {
	'1': u"~!@#&#38;%^&&#38;#120162;&#38;#120168;&#38;#120150;&#38;#120163;&#38;#120165;&#38;#120170;&#38;#120166;&#38;#120154;&#38;#120160;&#38;#120161;[]&#38;#120146;&#38;#120164;&#38;#120149;&#38;#120151;&#38;#120152;&#38;#120153;&#38;#120155;&#38;#120156;&#38;#120157;;'&#38;#120171;&#38;#120169;&#38;#120148;&#38;#120167;&#38;#120147;&#38;#120159;&#38;#120158;,./ℚ&#38;#120142;&#38;#120124;ℝ&#38;#120139;&#38;#120144;&#38;#120140;&#38;#120128;&#38;#120134;ℙ{}&#38;#120120;&#38;#120138;&#38;#120123;&#38;#120125;&#38;#120126;ℍ&#38;#120129;&#38;#120130;&#38;#120131;:\"|ℤ&#38;#120143;ℂ&#38;#120141;&#38;#120121;ℕ&#38;#120132;<>?", 
	'2': u"~!@#&#38;%^&&#38;#120474;&#38;#120480;&#38;#120462;&#38;#120475;&#38;#120477;&#38;#120482;&#38;#120478;&#38;#120466;&#38;#120472;&#38;#120473;[]&#38;#120458;&#38;#120476;&#38;#120461;&#38;#120463;&#38;#120464;&#38;#120465;&#38;#120467;&#38;#120468;&#38;#120469;;'&#38;#120483;&#38;#120481;&#38;#120460;&#38;#120479;&#38;#120459;&#38;#120471;&#38;#120470;,./&#38;#120448;&#38;#120454;&#38;#120436;&#38;#120449;&#38;#120451;&#38;#120456;&#38;#120452;&#38;#120440;&#38;#120446;&#38;#120447;{}&#38;#120432;&#38;#120450;&#38;#120435;&#38;#120437;&#38;#120438;&#38;#120439;&#38;#120441;&#38;#120442;&#38;#120443;:\"|&#38;#120457;&#38;#120455;&#38;#120434;&#38;#120453;&#38;#120433;&#38;#120445;&#38;#120442;<>?", 
	'3': u"~!@#&#38;%^&&#38;#120006;&#38;#120012;ℯ&#38;#120007;&#38;#120009;&#38;#120014;&#38;#120010;&#38;#119998;ℴ&#38;#120005;[]&#38;#119990;&#38;#120008;&#38;#119993;&#38;#119995;ℊ&#38;#119997;&#38;#119999;&#38;#120000;&#38;#120001;;'&#38;#120015;&#38;#120013;&#38;#119992;&#38;#120011;&#38;#119991;&#38;#120003;&#38;#120002;,./&#38;#119980;&#38;#119986;ℰℛ&#38;#119983;&#38;#119988;&#38;#119984;ℐ&#38;#119978;&#38;#119979;{}&#38;#119964;&#38;#119982;&#38;#119967;ℱ&#38;#119970;ℋ&#38;#119973;&#38;#119974;ℒ:\"|&#38;#119989;&#38;#119987;&#38;#119966;&#38;#119985;ℬ&#38;#119977;ℳ<>?", 
	'4': u"~!@#&#38;%^&&#38;#120058;&#38;#120064;&#38;#120046;&#38;#120059;&#38;#120061;&#38;#120066;&#38;#120062;&#38;#120050;&#38;#120056;&#38;#120057;[]&#38;#120042;&#38;#120060;&#38;#120045;&#38;#120047;&#38;#120048;&#38;#120049;&#38;#120051;&#38;#120052;&#38;#120053;;'&#38;#120067;&#38;#120065;&#38;#120044;&#38;#120063;&#38;#120043;&#38;#120055;&#38;#120054;,./&#38;#120032;&#38;#120038;&#38;#120020;&#38;#120033;&#38;#120035;&#38;#120040;&#38;#120036;&#38;#120024;&#38;#120030;&#38;#120031;{}&#38;#120016;&#38;#120034;&#38;#120019;&#38;#120021;&#38;#120022;&#38;#120023;&#38;#120025;&#38;#120026;&#38;#120027;:\"|&#38;#120041;&#38;#120039;&#38;#120018;&#38;#120037;&#38;#120017;&#38;#120029;&#38;#120028;<>?", 
	'5': u"~¡@#&#38;%^&bʍǝɹʇʎnᴉod[]ɐspɟƃɥɾʞl;'zxɔʌquɯ,./bʍǝɹʇʎnᴉod{}ɐspɟƃɥɾʞl:\"|zxɔʌquɯ<>¿", 
	'6': u"~!@#&#38;%^&ǫᴡᴇʀᴛʏᴜɪᴏᴘ[]ᴀsᴅғɢʜᴊᴋʟ;'ᴢxᴄᴠʙɴᴍ,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?", 
	'7': u"~!@#&#38;%^&ᑫᗯᗴᖇTYᑌIOᑭ[]ᗩՏᗪᖴᘜᕼᒍKᒪ;'ᘔ᙭ᑕᐯᗷᑎᗰ,./ᑫᗯᗴᖇTYᑌIOᑭ{}ᗩՏᗪᖴᘜᕼᒍKᒪ:\"|ᘔ᙭ᑕᐯᗷᑎᗰ<>?", 
	'8': u"~!@#&#38;%^&&#38;#119850;&#38;#119856;&#38;#119838;&#38;#119851;&#38;#119853;&#38;#119858;&#38;#119854;&#38;#119842;&#38;#119848;&#38;#119849;[]&#38;#119834;&#38;#119852;&#38;#119837;&#38;#119839;&#38;#119840;&#38;#119841;&#38;#119843;&#38;#119844;&#38;#119845;;'&#38;#119859;&#38;#119857;&#38;#119836;&#38;#119855;&#38;#119835;&#38;#119847;&#38;#119846;,./&#38;#119824;&#38;#119830;&#38;#119812;&#38;#119825;&#38;#119827;&#38;#119832;&#38;#119828;&#38;#119816;&#38;#119822;&#38;#119823;{}&#38;#119808;&#38;#119826;&#38;#119811;&#38;#119813;&#38;#119814;&#38;#119815;&#38;#119817;&#38;#119818;&#38;#119819;:\"|&#38;#119833;&#38;#119831;&#38;#119810;&#38;#119829;&#38;#119809;&#38;#119821;&#38;#119820;<>?", 
	'9': u"~!@#&#38;%^&&#38;#119902;&#38;#119908;&#38;#119890;&#38;#119903;&#38;#119905;&#38;#119910;&#38;#119906;&#38;#119894;&#38;#119900;&#38;#119901;[]&#38;#119886;&#38;#119904;&#38;#119889;&#38;#119891;&#38;#119892;ℎ&#38;#119895;&#38;#119896;&#38;#119897;;'&#38;#119911;&#38;#119909;&#38;#119888;&#38;#119907;&#38;#119887;&#38;#119899;&#38;#119898;,./&#38;#119876;&#38;#119882;&#38;#119864;&#38;#119877;&#38;#119879;&#38;#119884;&#38;#119880;&#38;#119868;&#38;#119874;&#38;#119875;{}&#38;#119860;&#38;#119878;&#38;#119863;&#38;#119865;&#38;#119866;&#38;#119867;&#38;#119869;&#38;#119870;&#38;#119871;:\"|&#38;#119885;&#38;#119883;&#38;#119862;&#38;#119881;&#38;#119861;&#38;#119873;&#38;#119872;<>?", 
	'10': u"~!@#&#38;%^&&#38;#119954;&#38;#119960;&#38;#119942;&#38;#119955;&#38;#119957;&#38;#119962;&#38;#119958;&#38;#119946;&#38;#119952;&#38;#119953;[]&#38;#119938;&#38;#119956;&#38;#119941;&#38;#119943;&#38;#119944;&#38;#119945;&#38;#119947;&#38;#119948;&#38;#119949;;'&#38;#119963;&#38;#119961;&#38;#119940;&#38;#119959;&#38;#119939;&#38;#119951;&#38;#119950;,./&#38;#119928;&#38;#119934;&#38;#119916;&#38;#119929;&#38;#119931;&#38;#119936;&#38;#119932;&#38;#119920;&#38;#119926;&#38;#119927;{}&#38;#119912;&#38;#119930;&#38;#119915;&#38;#119917;&#38;#119918;&#38;#119919;&#38;#119921;&#38;#119922;&#38;#119923;:\"|&#38;#119937;&#38;#119935;&#38;#119914;&#38;#119933;&#38;#119913;&#38;#119925;&#38;#119924;<>?", 
	'11': u"~!@#&#38;%^&ⓆⓌⒺⓇⓉⓎⓊⒾⓄⓅ[]ⒶⓈⒹⒻⒼⒽⒿⓀⓁ;'ⓏⓍⒸⓋⒷⓃ ,./ⓆⓌⒺⓇⓉⓎⓊⒾⓄⓅ{}ⒶⓈⒹⒻⒼⒽⒿⓀⓁ:\"|ⓏⓍⒸⓋⒷⓃ <>?", 
	'12': u"~!@#&#38;%^&🅠🅦🅔🅡🅣🅨🅤🅘🅞🅟[]🅐🅢🅓🅕🅖🅗🅙🅚🅛;'🅩🅧🅒🅥🅑🅝🅜,./🅠🅦🅔🅡🅣🅨🅤🅘🅞🅟{}🅐🅢🅓🅕🅖🅗🅙🅚🅛:\"|🅩🅧🅒🅥🅑🅝🅜<>?", 
	'13': u"~!@#&#38;%^&🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿[]🄰🅂🄳🄵🄶🄷🄹🄺🄻;'🅉🅇🄲🅅🄱🄽🄼,./🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿{}🄰🅂🄳🄵🄶🄷🄹🄺🄻:\"|🅉🅇🄲🅅🄱🄽🄼<>?", 
	'14': u"~!@#&#38;%^&&#38;#120110;&#38;#120116;&#38;#120098;&#38;#120111;&#38;#120113;&#38;#120118;&#38;#120114;&#38;#120102;&#38;#120108;&#38;#120109;[]&#38;#120094;&#38;#120112;&#38;#120097;&#38;#120099;&#38;#120100;&#38;#120101;&#38;#120103;&#38;#120104;&#38;#120105;;'&#38;#120119;&#38;#120117;&#38;#120096;&#38;#120115;&#38;#120095;&#38;#120107;&#38;#120106;,./&#38;#120084;&#38;#120090;&#38;#120072;ℜ&#38;#120087;&#38;#120092;&#38;#120088;ℑ&#38;#120082;&#38;#120083;{}&#38;#120068;&#38;#120086;&#38;#120071;&#38;#120073;&#38;#120074;ℌ&#38;#120077;&#38;#120078;&#38;#120079;:\"|ℨ&#38;#120091;ℭ&#38;#120089;&#38;#120069;&#38;#120081;&#38;#120080;<>?", 
	'15': u"~!@#&#38;%^&&#38;#120214;&#38;#120220;&#38;#120202;&#38;#120215;&#38;#120217;&#38;#120222;&#38;#120218;&#38;#120206;&#38;#120212;&#38;#120213;[]&#38;#120198;&#38;#120216;&#38;#120201;&#38;#120203;&#38;#120204;&#38;#120205;&#38;#120207;&#38;#120208;&#38;#120209;;'&#38;#120223;&#38;#120221;&#38;#120200;&#38;#120219;&#38;#120199;&#38;#120211;&#38;#120210;,./&#38;#120188;&#38;#120194;&#38;#120176;&#38;#120189;&#38;#120191;&#38;#120196;&#38;#120192;&#38;#120180;&#38;#120186;&#38;#120187;{}&#38;#120172;&#38;#120190;&#38;#120175;&#38;#120177;&#38;#120178;&#38;#120179;&#38;#120181;&#38;#120182;&#38;#120183;:\"|&#38;#120197;&#38;#120195;&#38;#120174;&#38;#120193;&#38;#120173;&#38;#120185;&#38;#120184;<>?"
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
