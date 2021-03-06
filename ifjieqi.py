import jieqi

def panduan(jq):
    jq=jq
    if jq=='立春':
        bz="立春，为二十四节气之首。立，是“开始”之意；春，代表着温暖、生长。二十四节气最初是依据“斗转星移”制定，当北斗七星的斗柄指向寅位时为立春。现行是依据太阳黄经度数定节气，当太阳到达黄经315°时为立春，于每年公历2月3-5日交节。干支纪元，以寅月为春正、立春为岁首，立春乃万物起始、一切更生之义也，意味着新的一个轮回已开启。在传统观念中，立春有吉祥的涵义。立春标志着万物闭藏的冬季已过去，开始进入风和日暖、万物生长的春季。在自然界，立春最显著的特点就是万物开始有复苏的迹象。时至立春，在我国的北回归线（黄赤交角）及其以南一带，可明显感觉到早春的气息。由于我国幅员辽阔，南北跨度大，各地自然节律不一，“立春”对于很多地区来讲只是入春天的前奏，万物尚未复苏，还处于万物闭藏的冬天。立春，意味着万物闭藏的冬季已过去，开始进入风和日暖、万物生长的春季。由于我国幅员辽阔，各地的气候相差悬殊，“立”的具体气候意义并不适用于全国各地，所对应的地域是位于北回归线上的岭南地区。冬春的分界线，在广西桂林到江西赣州一线，当立春时，那一线以南地区，已有春的气息了；但我国93%的陆地面积上都还是冬，到黑龙江，往往是在谷雨或立夏时才入春。"
    else:
        if jq=='雨水':
            bz='雨水，是二十四节气之第2个节气。斗指壬；太阳到达黄经330°；每年公历2月18-20日交节。雨水节气的含义是降雨开始，降雨量级多以小雨或毛毛细雨为主。俗话说“春雨贵如油”，适宜的降水对农作物的生长很重要，它是农耕文化对于节令的反映。进入雨水节气，我国北方地区尚未有春天气息，南方大多数地方则是春意盎然，一幅早春的景象。雨水节气时段一般从公历2月18日至20日开始，到3月4日或5日结束。时至雨水节气，太阳的直射点也由南半球逐渐向赤道靠近了，这时的北半球，日照时数和强度都在增加，气温回升较快，来自海洋的暖湿空气开始活跃，并渐渐向北挺进与冷空气相遇，形成降雨。雨水时节，天气变化不定，是全年寒潮过程出现最多的时节之一，忽冷忽热，乍暖还寒。雨水节气标示着降雨开始、雨量渐增，俗话说“春雨贵如油”，适宜的降水对农作物的生长很重要。进入雨水节气，我国北方阴寒未尽，一些地方仍下雪，尚未入春，仍是很冷；南方大多数地方则是春意盎然，一幅早春的景象。雨水节气后，太阳的直射点也由南半球逐渐向赤道靠近了，这时的北半球，日照时数和强度都在增加，气温回升较快，来自海洋的暖湿空气开始活跃，并渐渐向北挺进，降雨逐渐增多，但降雨量级多以小雨或毛毛细雨为主。中国气候学上，常以每五天的日平均气温稳定在10℃以上的始日划分为春季开始。'
        else:

            if jq == '惊蛰':
                bz = '惊蛰，意指天气回暖、春雷始鸣，惊醒蛰伏于地下冬眠的昆虫，一年的春耕也由此开始。同时，全国大部分地区气温快速回升，将迎来一派融融春光。是二十四节气中的第三个节气。惊蛰反映的是自然生物受节律变化影响而出现萌发生长的现象。时至惊蛰，阳气上升、气温回暖、春雷乍动、雨水增多，万物生机盎然。农耕生产与大自然的节律息息相关，惊蛰节气在农耕上有着相当重要的意义，它是古代农耕文化对于自然节令的反映。惊蛰时节，春气萌动，大自然有了新的活力。所谓“春雷惊百虫”，是指惊蛰时节，春雷始鸣，惊醒蛰伏于地下越冬的蛰虫。惊蛰节气的标志性特征是春雷乍动、万物生机盎然。'
            else:
                if jq == '春分':
                    bz = '春分，太阳直射赤道，南北半球昼夜平分。此后，气候逐渐温和,雨水充沛，阳光明媚，中国大部分地区的越冬作物进入春季生长阶段，早稻开始播种。春季第四个节气。于每年公历3月19-22日交节。春分在天文学上有重要意义，春分这天南北半球昼夜平分，自这天以后太阳直射位置继续由赤道向北半球推移，北半球各地白昼开始长于黑夜，南半球与之相反。在气候上，也有比较明显的特征，我国除青藏高原、东北、西北和华北北部地区外均进入了明媚的春天。春分的意义，一是指一天时间白天黑夜平分，各为12小时；二是古时以立春至立夏为春季，春分正当春季3个月之中，平分了春季。春分后，气候温和，雨水充沛，阳光明媚。春分时节，我国民间有放风筝、吃春菜、立蛋等风俗。'
                else:
                    if jq == '清明':
                        bz = '清明节，中国传统节日，又称踏青节、行清节、三月节、祭祖节等，节期在仲春与暮春之交，既是自然节气点，也是传统节日。扫墓祭祖是清明节的礼俗主题，在中国自古传承,至今不辍。清明节源自上古时代的祖先信仰与春祭礼俗，兼具自然与人文两大内涵，既是自然节气点，也是传统节日。清明节是传统的重大春祭节日，扫墓祭祀、缅怀祖先，是中华民族自古以来的优良传统，不仅有利于弘扬孝道亲情、唤醒家族共同记忆，还可促进家族成员乃至民族的凝聚力和认同感。清明节融汇自然节气与人文风俗为一体，是天时地利人和的合一，充分体现了中华民族先祖们追求“天、地、人”的和谐合一，讲究顺应天时地宜、遵循自然规律的思想。清明节的节俗丰富，扫墓祭祖与踏青郊游是清明节的两大礼俗主题，这两大传统礼俗主题在中国自古传承，至今不辍。'
                    else:
                        if jq == '谷雨':
                            bz = '谷雨，是二十四节气之第6个节气，春季的最后一个节气。斗指辰；太阳黄经为30°；于每年公历4月19日—21日交节。谷雨取自“雨生百谷“之意，此时降水明显增加，田中的秧苗初插、作物新种，最需要雨水的滋润，降雨量充足而及时，谷类作物能茁壮成长。谷雨时节，在中国南方地区，往往开始明显多雨，而特别是华南，一旦冷空气与暖湿空气交汇，往往形成较长时间的降雨天气。秦岭—淮河是南方春雨和北方春旱区之间的过渡地区，从秦岭-淮河附近向北，春雨急剧减少。在北方地区，谷雨是“终霜”的象征。由于谷雨节气后降雨增多，空气中的湿度逐渐加大，应注意预防“湿邪”侵袭伤身。民间在谷雨节气摘谷雨茶、走谷雨、吃春、赏花等习俗。俗话说：“雨生百谷”。雨量充足而及时，谷类作物能够茁壮生长。谷雨节气就有这样的涵义。'
                        else:
                            if jq == '立夏':
                                bz = '立夏，是二十四节气中的第7个节气，夏季的第一个节气，交节时间在每年公历5月05-07日。此时北斗七星的斗柄指向东南方，太阳黄经达45°。立夏，气温显著升高，炎暑将临，雷雨增多，是标示万物进入旺季生长的一个重要节气。立夏后，日照增加，逐渐升温，雷雨增多，农作物进入了茁壮成长阶段。进入立夏时节，人们的新陈代谢加快，心脑血液供给不足，常使人烦躁不安，倦怠懒散。立夏之后，天气逐渐转热，饮食宜清淡，应以易消化、富含维生素的食物为主，大鱼大肉和油腻辛辣的食物要少吃。立夏以后饮食原则是“春夏养阳”，养阳重在养心，养心可多喝牛奶、多吃豆制品、鸡肉、瘦肉等，既能补充营养，又起到强心的作用。'
                            else:
                                if jq == '小满':
                                    bz = '是夏季的第二个节气。小满，斗指甲，太阳达黄经60°，于每年公历5月20－22日交节。小满节气意味着进入了大幅降水的雨季，雨水开始增多，往往会出现持续大范围的强降水。小满和雨水、谷雨、小雪、大雪等一样，都是直接反映降水的节气。小满反映了降雨量大的气候特征：“小满江河满”（南方）。另有解释是指北方夏熟作物的籽粒开始灌浆饱满，但还未成熟，只是小满，还未大满（北方）。小满节气期间，我国南方地区一般会降雨多、雨量大。由于南方暖湿气流活跃，与从北方南下的冷空气在黄赤交角处的华南一带交汇，这时华南地区往往会出现持续大范围的强降水，造成暴雨或特大暴雨，正如民谚云“小满，江河易满”。江南地区往往也是江河湖满，如果这个阶段雨水偏少，可能是太平洋的副热带高压势力较弱，位置偏南，意味着到了黄梅时节。在北方，小满节气期间降雨很少或无雨，这期间气温上升很快，与南方的温差进一步缩小。'
                                else:
                                    if jq == '芒种':
                                        bz = '芒种时，北斗指向已。太阳黄经为75°。这时最适合播种有芒的谷类作物，如晚谷、黍、稷等。如过了这个时候再种有芒和作物就不好成熟了。同时，“芒”指有芒作物如小麦、大麦等，“种”指种子。芒种即表明小麦等有芒作物成熟。芒种前后，我国中部的长江中、下游地区，雨量增多，气温升高，进入连绵阴雨的梅雨季节，空气非常潮湿，天气异常闷热，各种器具和衣物容易发霉，所以在我国长江中、下游地区也叫“霉雨”。芒种是表征麦类等有芒作物的成熟，是一个反映农业物候现象的节气。时至芒种，四川盆地麦收季节已经过去，中稻、红苕移栽接近尾声。大部地区中稻进入返青阶段，秧苗嫩绿，一派生机。“东风染尽三千顷，折鹭飞来无处停”的诗句，生动的描绘了这时田野的秀丽景色。'
                                    else:
                                        if jq == '夏至':
                                            bz = '夏至，是二十四节气的第10个节气。斗指午；太阳黄经90°；于公历6月21-22日交节。夏至是太阳北行的转折点，夏至这天过后太阳将走"回头路"，太阳光直射点开始从北回归线向南移动。对于我国位于北回归线以北的地区来说，夏至日过后，正午太阳高度开始逐日降低;对于我国位于北回归线以南的地区来说，夏至日过后，正午太阳高度经过南返的太阳直射后才开始逐日降低。夏至在中夏之位，即午位，午属阳；夏至虽然阳气较盛，且白昼最长，但却未必是一年中最热的一天，因此时接近地表的热量仍在积蓄，并没有达到最多的时候。夏至以后地面受热强烈，空气对流旺盛，易形成雷阵雨。夏至既是二十四节气之一，古时也是民间“四时八节”中的一个节日，自古民间有在夏至拜神祭祖的习俗。此外，夏至后，人们普遍会食用清补凉汤、凉茶、酸梅汤等来避暑。夏至日过后，北回归线及其以北的地区，正午太阳高度角也开始逐日降低。同时，夏至到来后，夜空星象也逐渐变成夏季星空。'
                                        else:
                                            if jq == '小暑':
                                                bz = '小暑，是第十一个节气，干支历午月的结束以及未月的起始。斗指辛，太阳到达黄经105度，于每年公历7月6-8日交节。暑，是炎热的意思，小暑为小热，还不十分热。意指天气开始炎热，但还没到最热。小暑虽不是一年中最炎热的季节，但紧接着就是一年中最热的节气大暑，民间有“小暑大暑，上蒸下煮”之说。我国多地自小暑起进入雷暴最多的时节。小暑开始进入伏天，所谓“热在三伏”，三伏天通常出现在小暑与处暑之间，是一年中气温最高且又潮湿、闷热的时段。季风气候是我国气候的主要特点，夏季受来自海洋暖湿气流的影响，我国多地高温潮湿多雨。这个时节虽然阳光猛烈、高温潮湿多雨，但对于农作物来讲，雨热同期有利于成长。在过去我国南方地区民间有小暑“食新”习俗，即在小暑过后尝新米，农民将新割的稻谷碾成米后，做好饭供祀五谷大神和祖先，然后人人吃尝新酒等。在北方地区有头伏吃饺子的传统，伏日人们食欲不振，往往比常日消瘦，俗谓之苦夏，而饺子在传统习俗里正是开胃解馋的食物，且饺子的外形像元宝，有“元宝藏福”的意思，吃饺子象征着福气满满。'
                                            else:
                                                if jq == '大暑':
                                                    bz = '大暑，二十四节气之一，夏季最后一个节气。小暑后十五日斗指未为大暑；太阳黄经为120°；公历7月22—24日交节。“暑”是炎热的意思，大暑，指炎热之极。大暑相对小暑，更加炎热，是一年中日照最多、最炎热的节气，“湿热交蒸”在此时到达顶点。大暑气候特征：高温酷热，雷暴、台风频繁。大暑节气正值“三伏天”里的“中伏”前后，是一年中最热的时段。大暑时节阳光猛烈、高温潮湿多雨，虽不免有湿热难熬之苦，却十分有利于农作物成长，农作物在此期间成长最快。'
                                                else:
                                                    if jq == '立秋':
                                                        bz = '立秋，是二十四节气中第13个节气，秋季的第一个节气，一般在每年公历8月7或8日；此时北斗七星的斗柄指向西南，太阳到达黄经135°。整个自然界的变化是循序渐进的过程，立秋是阳气渐收，阴气渐长，由阳盛逐渐转变为阴盛的转折。在自然界，万物开始从繁茂成长趋向萧瑟成熟。立秋并不代表酷热天气就此结束，立秋还在暑热时段，尚未出暑，秋季第二个节气（处暑）才出暑，初秋期间天气仍然很热。所谓“热在三伏”，又有“秋后一伏”之说，立秋后还有至少“一伏”的酷热天气。按照“三伏”的推算方法，“立秋”这天往往还处在中伏期间，也就是说，酷暑并没有过完，真正有凉意一般要到白露节气之后。酷热与凉爽的分水岭并不是在立秋节气。进入秋季后，由夏季的多雨湿热过渡向秋季少雨干燥气候。在自然界中，阴阳之气开始转变，万物随阳气下沉而逐渐萧落。秋季最明显的变化草木的叶子从繁茂的绿色到发黄，并开始落叶，庄稼则开始成熟。'
                                                    else:
                                                        if jq == '处暑':
                                                            bz = '处暑，是二十四节气之第十四个节气。斗指戊（西南方）；太阳黄经达150°；于每年公历8月22-24日交节。处暑，即为“出暑”，是炎热离开的意思。时至处暑，太阳直射点继续南移、太阳辐射减弱，副热带高压也向南撤退，气温逐渐下降，暑气渐消。处暑意味着酷热难熬的天气到了尾声，这期间天气虽仍热，但已是呈下降趋势。处暑节气处在短期回热天气（秋老虎）期内，“秋老虎”一般发生在公历8月~9月之间，每年秋老虎的时间长短不一，总体来说持续半个月到二个月不等。处暑在日常生活中起到的意义，就是提醒人们暑气渐渐消退，天气由炎热向凉爽过渡，要注意预防“秋燥”。'
                                                        else:
                                                            if jq == '白露':
                                                                bz = '白露，是“二十四节气”中的第15个节气，秋季第3个节气，干支历申月的结束与酉月的起始。斗指癸；太阳达黄经165度；于公历9月7-9日交节。“白露”是反映自然界寒气增长的重要节气。由于天气逐渐转凉，白昼有阳光尚热，但傍晚后气温便很快下降，昼夜温差大。时至白露，夏季风逐渐为冬季风所代替，冷空气转守为攻，加上太阳直射点南移，北半球日照时间变短，光照强度减弱，地面辐射散热快，所以温度下降速度也逐渐加快。白露基本结束了暑天的闷热，天气渐渐转凉，寒生露凝。古人以四时配五行，秋属金，金色白，以白形容秋露，故名“白露”。中国古人根据对大自然的观察，将白露分为三候：“一候鸿雁来，二候玄鸟归，三候群鸟养羞。”意思是说这个节气，鸿雁与燕子等候鸟南飞避寒，百鸟开始贮存干果粮食以备过冬。这会儿农民也忙着收获庄稼，正所谓“抢秋抢秋，不抢就丢”。白露期间的各地民俗，主要有祭祀大禹、酿五谷酒、喝白露茶等。露是由于温度降低，水汽在地面或近地物体上凝结而成的水珠。所以，白露实际上是表征天气已经转凉。白露时节，秋风在降温的同时，把空气中的水分也吹干了，这种干燥的气候特点称为“秋燥”，白露的气候特点就是干燥。“白露”代表着暑热的结束，万物随寒气增长，逐渐萧落、成熟。'
                                                            else:
                                                                if jq == '秋分':
                                                                    bz = '秋分，是二十四节气之第十六个节气，秋季第四个节气。斗指酉；太阳达黄经180°；于每年的公历9月22-24日交节。秋分这天太阳几乎直射地球赤道，全球各地昼夜等长。秋分，“分”即为“平分”、“半”的意思，除了指昼夜平分外，还有一层意思是平分了秋季。秋分日后，太阳光直射位置南移，北半球昼短夜长，昼夜温差加大，气温逐日下降。秋分曾是传统的“祭月节”，中秋节由“秋夕祭月”演变而来。2018年6月21日，国务院关于同意设立“中国农民丰收节”的批复发布，同意自2018年起，将每年秋分设立为“中国农民丰收节”。'
                                                                else:
                                                                    if jq == '寒露':
                                                                        bz = '寒露，是二十四节气中的第十七个节气，属于秋季的第五个节气。斗指戊；太阳到达黄经195°；在每年公历10月7日－9日交节。寒露是一个反映气候变化特征的节气，寒露节气后，昼渐短，夜渐长，日照减少，热气慢慢退去，寒气渐生，昼夜的温差较大，晨晚略感丝丝寒意。从气候特点上看，寒露时节，南方秋意渐浓，气爽风凉，少雨干燥；北方广大地区已从深秋进入或即将进入冬季。寒露过后，我国南方大部分地区各地气温继续下降。华南日平均气温多不到20℃，即使在长江沿岸地区，气温也很难升到30℃以上，而最低气温却可降至10℃以下。由于全球气候变暖原因，气温下降日期或有所推迟。西北高原除了少数河谷低地以外，候（5天）平均气温普遍低于10℃，用气候学划分四季的标准衡量，已是冬季了，千里霜铺，与南方秋色迥然不同。'
                                                                    else:
                                                                        if jq == '霜降':
                                                                            bz = '霜降，是二十四节气中的第十八个节气，秋季的最后一个节气。斗指戌；太阳黄经为210°；于每年公历10月23—24日交节。进入霜降节气后，深秋景象明显，冷空气南下越来越频繁。霜降不是表示“降霜”，而是表示气温骤降、昼夜温差大。就全国平均而言，“霜降”是一年之中昼夜温差最大的时节。霜降时节，万物毕成，毕入于戌，阳下入地，阴气始凝，天气渐寒始于霜降。由于“霜”是天冷、昼夜温差变化大的表现，故以“霜降”命名这个表示“气温骤降、昼夜温差大”的节气。霜降节气特点是早晚天气较冷、中午则比较热，昼夜温差大，秋燥明显。'
                                                                        else:
                                                                            if jq == '立冬':
                                                                                bz = '立冬，二十四节气之一，斗柄指向西北，太阳黄经达225°，于公历11月7－8日之间交节。立冬是季节类节气，表示自此进入了冬季，意味着风雨、干湿、光照、气温等，处于转折点上，开始从秋季向冬季气候过渡。“秋收冬藏”，万物在冬季闭藏，冬季是享受丰收、休养生息的季节。立冬，是民间“四时八节”之一，在古代我国一些方会在立冬举行祭祀、饮宴等活动，作为重要的节日来庆贺。立，建始也；冬，终也，万物收藏也。冬天季节，阳退阴生，生气闭蓄，万物开始收藏。传统是以“立冬”作为冬季的开始，秋季少雨干燥气候渐过去，开始向阴雨寒冻的冬季气候过渡。立冬后日照时间将继续缩短，正午太阳高度继续降低，由于地表贮存的热量还有一定的能量，所以一般初冬（孟冬）时期气温虽逐渐下降，但还不是很冷；随着时间推移，强冷空气南下频繁，并越过南岭，天气越来越冷。在北方地区，立冬前就已很寒冷了。'
                                                                            else:
                                                                                if jq == '小雪':
                                                                                    bz = '小雪，是二十四节气中的第20个节气，冬季第2个节气，时间在每年公历11月22或23日，即太阳到达黄经240°时。小雪是反映降水与气温的节气，它是寒潮和强冷空气活动频数较高的节气。小雪节气的到来，意味着天气会越来越冷、降水量渐增。这个节气之所以叫小雪，是因为“雪”是寒冷天气的产物，这个节气期间的气候寒未深且降水未大，故用“小雪”来比喻这个节气期间的气候特征。“小雪”是个比喻，反映的是这个节气期间寒流活跃、降水渐增，不是表示这个节气下很小量的雪。小雪节气，东亚地区已建立起比较稳定的经向环流，西伯利亚地区常有低压或低槽，东移时会有大规模的冷空气南下，我国东南部会出现大范围大风降温天气。'
                                                                                else:
                                                                                    if jq == '大雪':
                                                                                        bz = '大雪，是二十四节气中的第21个节气，冬季的第三个节气。斗指癸，太阳到达黄经255度，交节时间为每年公历12月6-8日。大雪节气是干支历子月的起始，标志着仲冬时节正式开始。大雪节气与小雪节气一样，是反映气温与降水变化趋势的节气，它是古代农耕文化对于节令的反映。大雪是反映气候特征的一个节气，大雪节气的特点是气温显著下降、降水量增多。大雪节气是一个气候概念，它代表的是大雪节气期间的气候特征，即气温与降水量。节气大雪与天气大雪意义不同。实际上，大雪节气的雪却往往不如小雪节气来得大，全年下雪量最大的节气也不是在小雪、大雪节气。如在二十四节气圭表测影地黄河中下游地区，全年下雪最大的节气，既不是“小雪、大雪”，更不是“小寒、大寒”，而是在春季“雨水”节气。大雪节气下雪量并不是最大。'
                                                                                    else:
                                                                                        if jq == '冬至':
                                                                                            bz = '冬至，又称日南至、冬节、亚岁等，兼具自然与人文两大内涵，既是二十四节气中一个重要的节气，也是中国民间的传统祭祖节日。冬至是四时八节之一，被视为冬季的大节日，在古代民间有“冬至大如年”的讲法。冬至习俗因地域不同而又存在着习俗内容或细节上的差异。在中国南方地区，有冬至祭祖、宴饮的习俗。在中国北方地区，每年冬至日有吃饺子的习俗。冬至是“二十四节气”之第22个节气，斗指子，太阳黄经达270°，于每年公历12月21-23日交节。冬至是太阳直射点南行的极致，冬至这天太阳光直射南回归线，太阳光对北半球最为倾斜，太阳高度角最小，是北半球各地白昼最短、黑夜最长的一天。冬至也是太阳直射点北返的转折点，这天过后它将走“回头路”，太阳直射点开始从南回归线向北移动，北半球（我国位于北半球）白昼将会逐日增长。冬至这天，太阳虽低、白昼虽短，但是在气象上，冬至的温度并不是最低。实际上，由于地表尚有“积热”，冬至之前通常不会很冷，真正的严寒在冬至之后。由于我国各地的气候相差悬殊，这种气候意义的冬季对于我国多数地区来说，显然偏迟。时至冬至，标志着即将进入寒冷时节，民间由此开始“数九”计算寒天（民谚：“夏至三庚入伏，冬至逢壬数九）。'
                                                                                        else:
                                                                                            if jq == '小寒':
                                                                                                bz = '小寒，是二十四节气中的第23个节气，冬季的第5个节气，干支历子月的结束与丑月的起始。斗指子；太阳黄经为285°；于每年公历1月5-7日交节。冷气积久而寒，小寒是天气寒冷但还没有到极点的意思，它与大寒、小暑、大暑及处暑一样，都是表示气温冷暖变化的节气。小寒节气的特点就是寒冷，但是却还没有冷到极致。小寒时节，太阳直射点还在南半球，北半球的热量还处于散失的状态，白天吸收的热量还是少于夜晚释放的热量，因此北半球的气温还在持续降低。冬至之后，冷空气频繁南下，气温持续降低，温度在一年的小寒、大寒之际降到最低。民谚：“小寒时处二三九，天寒地冻冷到抖”，这说明了小寒节气的寒冷程度。根据我国长期以来的气象记录，在北方地区小寒节气比大寒节气更冷，在北方有“小寒胜大寒”一说；但对于南方部分地区，全年最低气温仍然会出现在大寒节气内。'
                                                                                            else:
                                                                                                bz = '大寒，是二十四节气中的最后一个节气。斗指丑；太阳黄经为300°；公历1月20－21日交节。同小寒一样，大寒也是表示天气寒冷程度的节气。在我国部分地区，大寒不如小寒冷，但在某些年份和沿海少数地方，全年最低汽温仍然会出现在大寒节气内。小寒、大寒是一年中雨水最少的时段。兹大寒一过，新一年的节气就又轮回来了，正所谓冬去春来。大寒虽然寒冷，但因为已近春天，所以不会像大雪到冬至期间那样酷寒。这时节，人们开始忙着除旧饰新、腌制年肴、准备年货和各种祭祀供品、扫尘洁物，因为中国人最重要的节日——春节就要到了。'







    return bz
