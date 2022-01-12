import nltk
import numpy as np
import re
import copy


from scipy import stats
from scipy.stats import spearmanr




#テキストの使いやすさ主成分レベル
tukaiyasusa = [-0.5236145389792606, -0.4655359338060707, -0.5934661265244124, -0.5325752208797596, -0.544835027673452, -0.473649285483764, -0.4855252715282002, -0.5332567216259921, -0.5785145596712252, -0.6012321762681648, -0.5590922850322703, -0.5553629552531629, -0.5592147430640036, -0.6310379622383117, -0.3825972434214442, -0.37256691070432674, -0.4912856797906177, -0.5678980176078031, -0.4557112973849606, -0.5812045399586855, -0.6033467246469859, -0.5108194762111643, -0.48117958397866967, -0.5415079541911073, -0.6174272645116979, -0.518755071122078, -0.5269403217133813, -0.4923316344162864, -0.5556927805929838, -0.415720890651899, -0.44014795647746796, -0.5105977492547465, -0.3974809112205476, -0.35382800902725037, -0.46659256181807507, -0.4595893360465726, -0.41669979121100265, -0.33238638562621464, -0.45383814904569836, -0.33958087430974454, -0.390568391413675, -0.3756659301820849, -0.33720135336393775, -0.44675101694915026, -0.3591712096868755, -0.44311032664238786, -0.4294275246117052, -0.5360974316146284, -0.38691403631561033, -0.3583856131840781, -0.4350007837965279, -0.40751208723452126, -0.3948005319689413, -0.4903777551255331, -0.36145944579491135, -0.3486231478114645, -0.3773203751307677, -0.3850075320578461, -0.34440633056028247, -0.2768546326672265, -0.4380728082505338, -0.36099131728277173, -0.39152454944438214, -0.390568391413675]

#参照の結束レベル
sansyou = [0.591405553384903, 0.38361685225026465, 0.33500300169459685, 0.5939302845203049, 0.5767839027813266, 0.31260969422089946, 0.5397822929210007, 0.38205837721466246, 0.32754393345977234, 0.3661598602377228, 0.2017402749717226, 0.24440403706431146, 0.2735092239823486, 0.35443633220988296, 0.4955703691881341, 0.5379118296421748, 0.4001143087357616, 0.22706402871121914, 0.5652472555857695, 0.4554099741977172, 0.33651917909153717, 0.253717487534163, 0.3488920133800174, 0.3698550470313139, 0.42129820183788774, 0.5695392874947258, 0.4024055005584878, 0.30379145716674255, 0.26657713695222635, 0.2821032175548873, 0.34988267029352726, 0.3028011671935562, 0.5407157609544878, 0.9431698303048406, 0.37236343062811655, 0.7676948233325541, 0.43757291751009514, 0.4949935505099778, 0.2616968293429297, 0.4590789900965414, 0.5838579521710108, 0.5514174431558126, 1.558792159321346, 0.7684817938514019, 0.5607813335655466, 0.724757695361868, 0.6835727345213184, 0.27858250984141864, 0.5509033936390865, 0.4273099764229459, 0.49080228902801554, 0.4662763715514708, 0.45754118211942, 0.610395032751177, 0.44535717151559023, 0.6210394233160226, 1.0353955915787094, 0.4225803493703733, 1.345122806004706, 0.6456666393045603, 0.4363300525369483, 1.4060472673715603, 0.555994538612926, 0.5838579521710108]

#LSAレベル
lsa = [0.8755897098670826, 0.8087680943206841, 0.8143358258672725, 0.8240539831958795, 0.8452087750220036, 0.745792016684205, 0.8442947227205497, 0.8114434220372848, 0.7825060835233111, 0.7828158948513061, 0.8167374536240879, 0.7706674382115534, 0.81015715129956, 0.7916623282511797, 0.8374288139570742, 0.8365834875383322, 0.7703888256237215, 0.734812662838856, 0.8474736632809662, 0.761748419749706, 0.7337840137995609, 0.7538640605070116, 0.7872178835813581, 0.8085486155406036, 0.8097041994631134, 0.8313301167070447, 0.7542986173008692, 0.7746075928845362, 0.8104236212365427, 0.7622643980471895, 0.7823036390782361, 0.7766042411916374, 0.8251633494336167, 0.8843296484485508, 0.45380282239292746, 0.8543184737245094, 0.4750982708375578, 0.8522018340310235, 0.5639448923203878, 0.7945886211711164, 0.7998426953860589, 0.8055976109201088, 0.8726052338285616, 0.7455558407704799, 0.6664965624353429, 0.8323524324849877, 0.8494867065560918, 0.5302441032398121, 0.6336281701431584, 0.5427189223700626, 0.512697068166298, 0.5939235837529449, 0.5765601562108038, 0.839802200013657, 0.622999887317614, 0.8211379283764922, 0.6726924057762792, 0.5803797206738733, 0.8286166827998694, 0.8463752646836395, 0.5358616429679555, 0.8683602159528553, 0.6527053672412003, 0.7998426953860589]

#連続語レベル
renzokugo = [19.943019943019944, 28.037383177570092, 26.08695652173913, 18.361581920903955, 9.202453987730062, 18.18181818181818, 21.70767004341534, 12.78772378516624, 11.574074074074073, 7.712082262210797, 2.7777777777777777, 19.37984496124031, 8.771929824561402, 11.494252873563218, 19.68503937007874, 23.762376237623762, 12.131715771230503, 2.3923444976076556, 20.442930153321974, 13.651877133105803, 0.0, 1.763668430335097, 10.080645161290322, 14.466546112115731, 23.166023166023166, 17.857142857142858, 5.167958656330749, 0.0, 7.042253521126761, 0.0, 3.3783783783783785, 0.0, 25.352293932179396, 23.426518819303453, 13.584288052373159, 20.4026299735647, 14.320785597381342, 24.078568178371, 12.700666587780539, 17.38673913714833, 17.92449565728918, 14.765691785612518, 18.94232449025431, 19.958140230228736, 14.011554552095092, 17.264879600181736, 16.121927583472825, 13.033175355450236, 13.27628264086056, 14.214529242066615, 12.692355551868596, 14.185631608720247, 15.354330708661417, 23.81639128105814, 12.674360971464985, 22.871763064040934, 23.545706371191137, 14.3166057713817, 16.084427349883974, 23.24374420759963, 13.074767895401855, 18.624305501212927, 15.074411905904944, 17.92449565728918]

#状況モデルレベル
zyoukyoumoderu = [0.9, 0.85, 0.8536585365853658, 0.9032258064516129, 0.9696969696969697, 0.6923076923076923, 0.9714285714285714, 0.8, 0.9090909090909091, 0.8695652173913043, 0.7741935483870968, 0.9629629629629629, 0.7142857142857143, 0.7941176470588235, 0.9473684210526315, 0.84375, 0.9310344827586207, 0.9523809523809523, 0.7307692307692307, 0.96, 0.7666666666666667, 0.78125, 0.7894736842105263, 0.9, 0.7058823529411765, 0.7058823529411765, 0.8666666666666667, 0.7941176470588235, 0.782608695652174, 0.7619047619047619, 0.9411764705882353, 0.9090909090909091, 0.8645465253239105, 0.894649751792609, 0.9492682926829268, 0.9079110012360939, 0.993020304568528, 0.8840952994204765, 0.9359415305245056, 0.8853427895981087, 0.9515738498789347, 0.8851963746223565, 0.9709737827715356, 0.9767441860465116, 0.9945137157107232, 0.8972477064220183, 0.9556213017751479, 0.9481090589270009, 0.996134732192159, 0.9890480202190396, 0.9712389380530974, 0.9938949938949939, 0.9954086317722681, 0.9036729036729036, 0.9938737040527804, 0.9355948869223205, 0.9666666666666667, 0.9929462832338578, 0.9413754227733935, 0.9142108709888671, 0.9931093884582257, 0.9579500657030223, 0.9981000633312223, 0.9515738498789347]

#構文パターン密度レベル
koubun = [119.65811965811966, 65.42056074766354, 69.56521739130434, 91.80790960451978, 96.62576687116564, 76.92307692307693, 99.85528219971057, 107.41687979539643, 55.55555555555555, 79.69151670951156, 19.444444444444446, 60.077519379844965, 57.89473684210526, 65.13409961685824, 102.36220472440945, 95.04950495049505, 69.32409012131716, 64.5933014354067, 100.51107325383305, 85.32423208191128, 61.696658097686374, 51.14638447971781, 40.32258064516129, 68.71609403254973, 113.8996138996139, 105.15873015873017, 67.18346253229974, 69.97084548104957, 38.73239436619718, 30.100334448160535, 33.78378378378378, 67.21311475409836, 73.22566115436587, 94.79931282211464, 57.201309328968904, 73.20544973903613, 79.60538279687215, 87.47914454724707, 63.46388987496548, 88.8792810598808, 94.88217585383578, 78.77626091236432, 143.103147071302, 120.7205860367768, 79.62016070124179, 107.8802564490888, 107.30332129327813, 78.25056665979805, 64.90182748830328, 70.54812483608707, 67.73404122941639, 78.67368695879205, 77.03412073490813, 75.73447608059665, 69.17793669900163, 88.25657724711841, 96.49122807017544, 71.35933189173068, 123.01726056136559, 73.95736793327156, 66.63736746690107, 121.5275060646373, 74.26788286125779, 94.88217585383578]

#単語情報レベル
tangozyouhou = [51.28205128205128, 10.903426791277258, 31.30434782608696, 38.13559322033898, 3.067484662576687, 50.349650349650354, 4.341534008683069, 5.115089514066496, 9.25925925925926, 12.853470437017995, 127.77777777777777, 19.37984496124031, 84.21052631578947, 72.79693486590038, 0.0, 81.1881188118812, 51.99306759098787, 28.70813397129187, 44.29301533219761, 10.238907849829351, 28.27763496143959, 26.455026455026452, 8.064516129032258, 25.31645569620253, 11.583011583011583, 5.952380952380952, 25.839793281653744, 45.18950437317784, 45.774647887323944, 15.050167224080267, 27.027027027027028, 8.196721311475411, 16.601248310919505, 18.09047842157322, 45.00818330605565, 21.351589507218872, 53.418803418803414, 20.741695737903836, 74.58683390525776, 40.14699978382385, 19.37783314301533, 55.0216304432298, 0.8235793256632309, 4.858723277021976, 41.20459525864931, 40.8400222121258, 19.99823804070126, 60.32351123016691, 49.146239053065145, 33.46446367689483, 51.474553071467085, 57.1341543013794, 49.54068241469816, 12.19662944497095, 55.37067195355094, 25.481986871349562, 20.77562326869806, 46.454403101931256, 11.888489780349026, 15.68118628359592, 49.8818876009449, 24.141169105563815, 55.640902544407105, 19.37783314301533]


level_soukan_dic={"３つの接続詞のzスコア": 0.6599890232784251, "隣接する文との内容語の重複の標準偏差": 0.5083065285904638, 
            "隣接する文のコサイン類似度": -0.18760245477022275,"時間的接続詞の発生率": 0.342612618128205,
            "時制の繰り返しの平均": 0.6285245987567255, "前置詞句の発生スコア": 0.3667653286504391,
            "一人称単数代名詞の発生率": 0.23318079080290005}

level_number_dic={0: "３つの接続詞のzスコア", 1: "隣接する文との内容語の重複の標準偏差", 2: "隣接する文のコサイン類似度",
                3: "時間的接続詞の発生率", 4: "時制の繰り返しの平均", 5: "前置詞句の発生スコア", 6: "一人称単数代名詞の発生率"}


level_sihyou_dic={0: tukaiyasusa, 1: sansyou, 2: lsa, 3: renzokugo,
            4: zyoukyoumoderu, 5: koubun, 6: tangozyouhou}



kazu=0
soukan=0
keisan_kaisuu=0
soukankekka={}
soukankekka_upper={}#相関が高かったものだけ入れるディクショナリ
while kazu < 6:

    keisan_kaisuu=kazu+1

    while keisan_kaisuu < 7:

        #相関計算
        x_np = np.array(level_sihyou_dic[kazu])
        y_np = np.array(level_sihyou_dic[keisan_kaisuu])


        #シャピロウィルク検定で正規性の確認
        #w値とp_value
        shap_w_x, shap_p_value_x = stats.shapiro(level_sihyou_dic[kazu])
        shap_w_y, shap_p_value_y = stats.shapiro(level_sihyou_dic[keisan_kaisuu])

        #p_valueが0.05以上なら，帰無仮説が採択→正規性がある
        if shap_p_value_x >= 0.05 and shap_p_value_y >= 0.05:
            #print("正規性があるといえる")

            #ピアソンの相関係数をとる
            # 相関行列を計算
            coef = np.corrcoef(x_np, y_np)
            soukan = coef[0][1]


        #p_valueが0.05以下なら，帰無仮説が棄却→正規性がない
        else:
            #print("正規性があるといえない")
   
            #スピアマンの順位相関係数
            correlation, pvalue = spearmanr(x_np, y_np)
            soukan = correlation

        
        soukankekka[level_number_dic[kazu]+ " - " + level_number_dic[keisan_kaisuu]] = soukan # パラメータ，相関の結果
        #相関が高かったら，ディクショナリに入れる
        if abs(soukan) >= 0.7:
            soukankekka_upper[level_number_dic[kazu]+ " - " + level_number_dic[keisan_kaisuu]] = soukan # パラメータ，相関の結果
        

        keisan_kaisuu+=1
        
    
    kazu+=1

    



#パラメータ番号と相関係数の結果を，相関係数の大きい順で表示
for s in soukankekka:
    print(s)
    print(soukankekka[s])
            
print("------")


#相関が0.7以上のものがあるか
if soukankekka_upper:
    print("相関係数が0.7以上あったもの")
    for s in soukankekka_upper:
        print(s)
        print(soukankekka_upper[s])
    print("------")

else:
    print("相関が高い組み合わせはありません")