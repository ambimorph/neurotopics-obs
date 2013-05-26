# Neurotopics/test/test_DocsToVocab

import unittest, StringIO

from scripts import DocsToVocab

class TestDocsToVocab(unittest.TestCase):

    def test_docs_to_vocab(self):

        full_text_file_name = 'data/sample_full_text_articles'
        doc_outfile_obj = StringIO.StringIO()
        voc_outfile_obj = StringIO.StringIO()
        dtv = DocsToVocab.DocsToVocab(full_text_file_name, doc_outfile_obj, voc_outfile_obj)
        dtv.docs_to_vocab()

        result = doc_outfile_obj.getvalue()
        expected_result = '\n'.join(["0:1 1:1 2:1 3:1 4:1 5:5 6:1 7:6 8:2 9:4 10:1 11:1 12:2 13:1 14:3 15:3 16:1 17:4 18:1 19:1 20:1 21:2 22:1 23:1 24:1 25:1 26:1 27:1 28:1 29:1 30:1 31:2 32:1 33:2 34:1 35:1 36:1 37:1 38:1 39:1 40:1 41:1 42:1 43:1 44:1 45:2 46:1 47:1 48:1 49:1 50:1 51:1 52:1 53:1 54:1 55:2 56:1 57:1 58:1 59:1 60:1 61:1 62:1 63:1 64:2 65:2 66:2 67:1 68:1 ", 
                                     "5:2 7:4 9:4 14:3 15:4 17:6 31:3 33:2 34:1 45:1 51:1 54:1 55:1 62:1 64:1 65:4 69:1 70:1 71:1 72:1 73:1 74:1 75:1 76:1 77:1 78:1 79:1 80:1 81:2 82:2 83:1 84:1 85:3 86:1 87:2 88:2 89:5 90:3 91:1 92:2 93:2 94:2 95:1 96:2 97:1 98:1 99:1 100:2 101:2 102:1 103:1 104:1 105:1 106:1 107:1 108:1 109:1 110:1 111:1 112:1 113:1 114:1 115:1 116:1 117:1 ",
                                     "128:1 129:1 130:1 131:1 132:1 133:2 134:4 7:5 136:3 137:3 138:1 139:4 140:1 13:3 142:1 15:5 144:1 17:8 146:1 147:1 148:1 149:1 150:1 151:2 152:1 153:1 154:1 155:2 5:5 157:1 158:1 31:4 160:1 33:4 162:1 163:2 164:1 165:1 166:2 167:1 168:1 145:1 170:1 135:3 172:1 173:1 174:1 9:6 159:1 161:1 141:1 156:1 169:1 143:1 94:1 103:1 171:1 118:1 119:2 120:1 121:1 122:2 123:1 124:2 125:1 126:1 127:1 ",
                                     "3:2 4:1 5:1 7:3 9:3 13:1 15:3 17:3 19:1 21:1 24:1 47:1 218:1 159:1 33:3 197:1 219:1 31:3 193:1 175:1 176:1 177:1 178:1 179:2 180:1 181:2 182:1 183:1 184:1 185:1 186:2 187:1 188:1 189:1 62:2 191:1 192:1 65:3 194:1 195:1 196:1 69:1 198:1 199:1 200:1 201:1 202:1 203:1 204:1 205:3 206:3 207:1 208:1 209:1 210:1 211:1 212:2 213:1 214:1 215:1 216:1 217:1 90:1 54:1 220:1 221:1 222:1 223:1 224:1 225:1 226:1 102:1 190:1 118:1 120:1 85:1 127:1 ",
                                     "256:1 257:1 2:1 3:1 260:1 5:7 262:1 7:2 264:2 9:1 266:1 267:1 268:1 13:2 15:3 16:1 17:1 259:1 151:2 25:1 103:1 31:1 33:1 36:1 38:1 42:2 263:1 114:1 261:1 54:2 265:1 65:3 75:1 258:1 247:1 76:1 79:1 85:2 227:6 228:2 229:1 230:1 231:1 232:1 233:1 234:1 235:1 236:1 237:1 238:1 239:1 240:1 241:1 242:1 243:2 244:1 245:1 246:1 119:1 248:1 249:1 250:1 251:1 252:2 253:1 254:1 255:1 \n"])

        self.assertEqual(result, expected_result, result)

        result = voc_outfile_obj.getvalue()

        expected_result = '\n'.join(["0 recent", "1 neuroimaging", "2 studies", "3 have", "4 shown", "5 the", "6 importance", "7 of", "8 prefrontal", "9 and", "10 anterior", "11 cingulate", "12 cortices", "13 in", "14 deception", "15 .", "16 however", "17 ,", "18 little", "19 is", "20 known", "21 about", "22 role", "23 each", "24 these", "25 regions", "26 during", "27 using", "28 positron", "29 emission", "30 tomography", "31 (", "32 pet", "33 )", "34 we", "35 measured", "36 brain", "37 activation", "38 while", "39 participants", "40 told", "41 truths", "42 or", "43 lies", "44 two", "45 types", "46 real-world", "47 events", "48 :", "49 experienced", "50 unexperienced", "51 imaging", "52 data", "53 revealed", "54 that", "55 activity", "56 dorsolateral", "57 ventrolateral", "58 medial", "59 was", "60 commonly", "61 associated", "62 with", "63 both", "64 pretending", "65 to", "66 know", "67 not", "68 whereas", "69 used", "70 functional", "71 magnetic", "72 resonance", "73 fmri", "74 determine", "75 whether", "76 neural", "77 can", "78 differentiate", "79 between", "80 true", "81 memory", "82 false", "83 subjects", "84 heard", "85 a", "86 series", "87 semantically", "88 related", "89 words", "90 were", "91 later", "92 asked", "93 make", "94 recognition", "95 judgment", "96 old", "97 nonstudied", "98 lures", "99 for", "100 unrelated", "101 new", "102 they", "103 also", "104 deceptive", "105 response", "106 half", "107 there", "108 3", "109 main", "110 findings", "111 first", "112 consistent", "113 notion", "114 executive", "115 function", "116 supports", "117 2", "118 introduction", "119 cognitive", "120 models", "121 normal", "122 word", "123 production", "124 picture", "125 naming", "126 has", "127 been", "128 segregated", "129 into", "130 several", "131 processing", "132 stages", "133 cf", "134 [", "135 levelt", "136 et", "137 al.", "138 1999", "139 ]", "140 indefrey", "141 2004", "142 ;", "143 see", "144 dell", "145 1997", "146 chiliant", "147 2003", "148 model", "149 visual", "150 object", "151 selection", "152 appropriate", "153 semantic", "154 representation", "155 lexical", "156 concept", "157 are", "158 followed", "159 by", "160 entry", "161 lemma", "162 retrieval", "163 encoding", "164 phonological", "165 form", "166 as", "167 well", "168 phonetic", "169 articulation", "170 name", "171 fig", "172 1", "173 interference", "174 paradigms", "175 human", "176 decision", "177 making", "178 guided", "179 predictions", "180 future", "181 comparisons", "182 those", "183 actual", "184 outcomes", "185 various", "186 learning", "187 identify", "188 what", "189 should", "190 be", "191 learned", "192 speed", "193 up", "194 experiments", "195 nonhuman", "196 primates", "197 schultz", "198 2000", "199 midbrain", "200 dopamine", "201 neurons", "202 fire", "203 according", "204 this", "205 prediction", "206 error", "207 signal", "208 i.e.", "209 firing", "210 rates", "211 elevated", "212 when", "213 animals", "214 received", "215 more", "216 valuable", "217 reward", "218 than", "219 expected", "220 positive", "221 decreased", "222 fell", "223 short", "224 expectations", "225 negative", "226 rewards", "227 language", "228 control", "229 refers", "230 mechanism", "231 controls", "232 which", "233 use", "234 at", "235 given", "236 moment", "237 context", "238 it", "239 allows", "240 bilinguals", "241 selectively", "242 communicate", "243 one", "244 target", "245 minimizing", "246 interferences", "247 from", "248 nontarget", "249 previous", "250 suggested", "251 participation", "252 different", "253 areas", "254 question", "255 remains", "256 among", "257 others", "258 relies", "259 on", "260 language-specific", "261 module", "262 general", "263 allow", "264 switching", "265 competing", "266 behavioral", "267 responses", "268 including\n"])

        self.assertListEqual(result.split(), expected_result.split())
       

if __name__ == '__main__':
    unittest.main()
