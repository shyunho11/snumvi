import pandas as pd
import re
import os
import glob
import ast
from shutil import copy2
import dicom2nifti

data_dir = "D:/Desktop/dicom"
output_dir = "D:/Desktop/HBP"
df = pd.read_csv("D:/Desktop/ser_found.csv").set_index("Number_폴더이름")

def copy_dicom(patient_id):
    series = df.loc[patient_id, 'ser']
    try:
        dest_dir = os.path.join(data_dir, str(patient_id) + '-2')
        if not os.path.exists(dest_dir):
            if series[0] == '[':
                dcm_files = [os.path.join(data_dir, str(patient_id), filename) for filename in ast.literal_eval(series)]
            else:
                dcm_files = glob.glob(os.path.join(data_dir, str(patient_id), series) + '*.dcm')
            
            os.makedirs(dest_dir)
            for file in dcm_files:
                copy2(file, os.path.join(dest_dir, os.path.basename(file)))
            print("Successfully copied to {}".format(dest_dir))
        else:
            #print("Copy failed: directory already exists.")
            pass
    except OSError:
        print("Error: failed to create {}".format(dest_dir))
    except TypeError:
        print("Error: invalid series name")

def dicoms2Nifti(patient_id, data_dir, output_dir):
    dicom_dir = os.path.join(data_dir, str(patient_id) + "-2")
    output_file = os.path.join(output_dir, str(patient_id) + ".nii.gz")
    try:
        dicom2nifti.dicom_series_to_nifti(dicom_dir, output_file, reorient_nifti=True)
        print("Successfully saved as {}".format(output_file))
    except:
        print("Conversion failed")

for patient_id in df.index:
    print(patient_id, end=":\t")
    copy_dicom(patient_id)
    dicoms2Nifti(patient_id, data_dir, output_dir)

import dicom2nifti.settings as settings
settings.disable_validate_slice_increment()

for patient_id in [34, 115]:
    print(patient_id, end=":\t")
    dicom_dir = os.path.join(data_dir, str(patient_id) + "-2")
    output_file = os.path.join(output_dir, str(patient_id) + ".nii.gz")
    dicom2nifti.dicom_series_to_nifti(dicom_dir, output_file, reorient_nifti=True)
    print("Successfully saved as {}".format(output_file))

"""
PS C:\Users\hyun-hoshin> & "C:/Users/hyun-hoshin/AppData/Local/Microsoft/WindowsApps/python3.8.exe" d:/Desktop/csv2nifti.py
1:      Successfully saved as D:/Desktop/HBP\1.nii.gz
2:      Successfully saved as D:/Desktop/HBP\2.nii.gz
3:      Successfully saved as D:/Desktop/HBP\3.nii.gz
7:      Successfully saved as D:/Desktop/HBP\7.nii.gz
10:     Successfully saved as D:/Desktop/HBP\10.nii.gz
11:     Successfully saved as D:/Desktop/HBP\11.nii.gz
16:     Successfully saved as D:/Desktop/HBP\16.nii.gz
17:     Successfully saved as D:/Desktop/HBP\17.nii.gz
20:     Successfully saved as D:/Desktop/HBP\20.nii.gz
21:     Successfully saved as D:/Desktop/HBP\21.nii.gz
22:     Successfully saved as D:/Desktop/HBP\22.nii.gz
23:     Successfully saved as D:/Desktop/HBP\23.nii.gz
24:     Successfully saved as D:/Desktop/HBP\24.nii.gz
26:     Successfully saved as D:/Desktop/HBP\26.nii.gz
27:     Successfully saved as D:/Desktop/HBP\27.nii.gz
28:     Successfully saved as D:/Desktop/HBP\28.nii.gz
29:     Successfully saved as D:/Desktop/HBP\29.nii.gz
33:     Successfully saved as D:/Desktop/HBP\33.nii.gz
Slice increment not consistent through all slices
---------------------------------------------------------
[-176.46180093 -174.65820312    1.17835999] [ 0.  0. -3.]
[-176.46180093 -174.65820312    7.17835999] [ 0.  0. -6.]
Instance Number: 27
---------------------------------------------------------
34:     Conversion failed
35:     Successfully saved as D:/Desktop/HBP\35.nii.gz
36:     Successfully saved as D:/Desktop/HBP\36.nii.gz
37:     Successfully saved as D:/Desktop/HBP\37.nii.gz
38:     Successfully saved as D:/Desktop/HBP\38.nii.gz
39:     Successfully saved as D:/Desktop/HBP\39.nii.gz
41:     Successfully saved as D:/Desktop/HBP\41.nii.gz
42:     Successfully saved as D:/Desktop/HBP\42.nii.gz
44:     Successfully saved as D:/Desktop/HBP\44.nii.gz
45:     Successfully saved as D:/Desktop/HBP\45.nii.gz
47:     Successfully saved as D:/Desktop/HBP\47.nii.gz
48:     Successfully saved as D:/Desktop/HBP\48.nii.gz
50:     Successfully saved as D:/Desktop/HBP\50.nii.gz
51:     Successfully saved as D:/Desktop/HBP\51.nii.gz
52:     Successfully saved as D:/Desktop/HBP\52.nii.gz
53:     Successfully saved as D:/Desktop/HBP\53.nii.gz
56:     Conversion failed
57:     Successfully saved as D:/Desktop/HBP\57.nii.gz
58:     Successfully saved as D:/Desktop/HBP\58.nii.gz
59:     Successfully saved as D:/Desktop/HBP\59.nii.gz
62:     Successfully saved as D:/Desktop/HBP\62.nii.gz
63:     Successfully saved as D:/Desktop/HBP\63.nii.gz
65:     Successfully saved as D:/Desktop/HBP\65.nii.gz
68:     Successfully saved as D:/Desktop/HBP\68.nii.gz
70:     Successfully saved as D:/Desktop/HBP\70.nii.gz
71:     Successfully saved as D:/Desktop/HBP\71.nii.gz
72:     Successfully saved as D:/Desktop/HBP\72.nii.gz
74:     Successfully saved as D:/Desktop/HBP\74.nii.gz
75:     Successfully saved as D:/Desktop/HBP\75.nii.gz
76:     Successfully saved as D:/Desktop/HBP\76.nii.gz
80:     Successfully saved as D:/Desktop/HBP\80.nii.gz
81:     Successfully saved as D:/Desktop/HBP\81.nii.gz
83:     Successfully saved as D:/Desktop/HBP\83.nii.gz
85:     Successfully saved as D:/Desktop/HBP\85.nii.gz
89:     Successfully saved as D:/Desktop/HBP\89.nii.gz
91:     Successfully saved as D:/Desktop/HBP\91.nii.gz
93:     Successfully saved as D:/Desktop/HBP\93.nii.gz
94:     Successfully saved as D:/Desktop/HBP\94.nii.gz
95:     Successfully saved as D:/Desktop/HBP\95.nii.gz
96:     Successfully saved as D:/Desktop/HBP\96.nii.gz
97:     Successfully saved as D:/Desktop/HBP\97.nii.gz
100:    Successfully saved as D:/Desktop/HBP\100.nii.gz
101:    Successfully saved as D:/Desktop/HBP\101.nii.gz
103:    Successfully saved as D:/Desktop/HBP\103.nii.gz
104:    Successfully saved as D:/Desktop/HBP\104.nii.gz
105:    Successfully saved as D:/Desktop/HBP\105.nii.gz
106:    Successfully saved as D:/Desktop/HBP\106.nii.gz
107:    Successfully saved as D:/Desktop/HBP\107.nii.gz
108:    Successfully saved as D:/Desktop/HBP\108.nii.gz
109:    Successfully saved as D:/Desktop/HBP\109.nii.gz
110:    Successfully saved as D:/Desktop/HBP\110.nii.gz
111:    Successfully saved as D:/Desktop/HBP\111.nii.gz
112:    Successfully saved as D:/Desktop/HBP\112.nii.gz
113:    Successfully saved as D:/Desktop/HBP\113.nii.gz
114:    Successfully saved as D:/Desktop/HBP\114.nii.gz
Slice increment not consistent through all slices
---------------------------------------------------------
[-161.52959856 -206.94041857  -61.45491028] [ 0.  0. -2.]
[-161.52959856 -206.94041857  -57.45491028] [ 0.  0. -4.]
Instance Number: 93
---------------------------------------------------------
115:    Conversion failed
116:    Successfully saved as D:/Desktop/HBP\116.nii.gz
117:    Successfully saved as D:/Desktop/HBP\117.nii.gz
120:    Successfully saved as D:/Desktop/HBP\120.nii.gz
121:    Successfully saved as D:/Desktop/HBP\121.nii.gz
122:    Successfully saved as D:/Desktop/HBP\122.nii.gz
123:    Successfully saved as D:/Desktop/HBP\123.nii.gz
124:    Successfully saved as D:/Desktop/HBP\124.nii.gz
125:    Successfully saved as D:/Desktop/HBP\125.nii.gz
127:    Successfully saved as D:/Desktop/HBP\127.nii.gz
128:    Successfully saved as D:/Desktop/HBP\128.nii.gz
129:    Successfully saved as D:/Desktop/HBP\129.nii.gz
130:    Successfully saved as D:/Desktop/HBP\130.nii.gz
133:    Successfully saved as D:/Desktop/HBP\133.nii.gz
134:    Successfully saved as D:/Desktop/HBP\134.nii.gz
138:    Successfully saved as D:/Desktop/HBP\138.nii.gz
140:    Successfully saved as D:/Desktop/HBP\140.nii.gz
141:    Successfully saved as D:/Desktop/HBP\141.nii.gz
142:    Successfully saved as D:/Desktop/HBP\142.nii.gz
143:    Successfully saved as D:/Desktop/HBP\143.nii.gz
144:    Successfully saved as D:/Desktop/HBP\144.nii.gz
145:    Successfully saved as D:/Desktop/HBP\145.nii.gz
146:    Successfully saved as D:/Desktop/HBP\146.nii.gz
149:    Successfully saved as D:/Desktop/HBP\149.nii.gz
153:    Successfully saved as D:/Desktop/HBP\153.nii.gz
154:    Successfully saved as D:/Desktop/HBP\154.nii.gz
157:    Successfully saved as D:/Desktop/HBP\157.nii.gz
158:    Successfully saved as D:/Desktop/HBP\158.nii.gz
159:    Successfully saved as D:/Desktop/HBP\159.nii.gz
161:    Successfully saved as D:/Desktop/HBP\161.nii.gz
162:    Successfully saved as D:/Desktop/HBP\162.nii.gz
163:    Successfully saved as D:/Desktop/HBP\163.nii.gz
168:    Successfully saved as D:/Desktop/HBP\168.nii.gz
171:    Successfully saved as D:/Desktop/HBP\171.nii.gz
176:    Successfully saved as D:/Desktop/HBP\176.nii.gz
177:    Successfully saved as D:/Desktop/HBP\177.nii.gz
178:    Successfully saved as D:/Desktop/HBP\178.nii.gz
179:    Successfully saved as D:/Desktop/HBP\179.nii.gz
180:    Successfully saved as D:/Desktop/HBP\180.nii.gz
181:    Successfully saved as D:/Desktop/HBP\181.nii.gz
182:    Successfully saved as D:/Desktop/HBP\182.nii.gz
185:    Successfully saved as D:/Desktop/HBP\185.nii.gz
186:    Successfully saved as D:/Desktop/HBP\186.nii.gz
187:    Successfully saved as D:/Desktop/HBP\187.nii.gz
188:    Successfully saved as D:/Desktop/HBP\188.nii.gz
189:    Successfully saved as D:/Desktop/HBP\189.nii.gz
190:    Successfully saved as D:/Desktop/HBP\190.nii.gz
191:    Successfully saved as D:/Desktop/HBP\191.nii.gz
192:    Successfully saved as D:/Desktop/HBP\192.nii.gz
193:    Successfully saved as D:/Desktop/HBP\193.nii.gz
194:    Successfully saved as D:/Desktop/HBP\194.nii.gz
195:    Successfully saved as D:/Desktop/HBP\195.nii.gz
196:    Successfully saved as D:/Desktop/HBP\196.nii.gz
197:    Successfully saved as D:/Desktop/HBP\197.nii.gz
198:    Successfully saved as D:/Desktop/HBP\198.nii.gz
199:    Conversion failed
200:    Successfully saved as D:/Desktop/HBP\200.nii.gz
201:    Successfully saved as D:/Desktop/HBP\201.nii.gz
202:    Successfully saved as D:/Desktop/HBP\202.nii.gz
204:    Successfully saved as D:/Desktop/HBP\204.nii.gz
205:    Successfully saved as D:/Desktop/HBP\205.nii.gz
207:    Successfully saved as D:/Desktop/HBP\207.nii.gz
208:    Successfully saved as D:/Desktop/HBP\208.nii.gz
210:    Successfully saved as D:/Desktop/HBP\210.nii.gz
212:    Successfully saved as D:/Desktop/HBP\212.nii.gz
213:    Successfully saved as D:/Desktop/HBP\213.nii.gz
215:    Successfully saved as D:/Desktop/HBP\215.nii.gz
217:    Successfully saved as D:/Desktop/HBP\217.nii.gz
218:    Successfully saved as D:/Desktop/HBP\218.nii.gz
220:    Successfully saved as D:/Desktop/HBP\220.nii.gz
221:    Successfully saved as D:/Desktop/HBP\221.nii.gz
222:    Successfully saved as D:/Desktop/HBP\222.nii.gz
223:    Successfully saved as D:/Desktop/HBP\223.nii.gz
224:    Successfully saved as D:/Desktop/HBP\224.nii.gz
225:    Successfully saved as D:/Desktop/HBP\225.nii.gz
226:    Successfully saved as D:/Desktop/HBP\226.nii.gz
227:    Successfully saved as D:/Desktop/HBP\227.nii.gz
229:    Successfully saved as D:/Desktop/HBP\229.nii.gz
231:    Successfully saved as D:/Desktop/HBP\231.nii.gz
232:    Successfully saved as D:/Desktop/HBP\232.nii.gz
233:    Successfully saved as D:/Desktop/HBP\233.nii.gz
234:    Successfully saved as D:/Desktop/HBP\234.nii.gz
237:    Successfully saved as D:/Desktop/HBP\237.nii.gz
239:    Successfully saved as D:/Desktop/HBP\239.nii.gz
240:    Successfully saved as D:/Desktop/HBP\240.nii.gz
241:    Successfully saved as D:/Desktop/HBP\241.nii.gz
242:    Successfully saved as D:/Desktop/HBP\242.nii.gz
243:    Successfully saved as D:/Desktop/HBP\243.nii.gz
244:    Successfully saved as D:/Desktop/HBP\244.nii.gz
246:    Successfully saved as D:/Desktop/HBP\246.nii.gz
249:    Successfully saved as D:/Desktop/HBP\249.nii.gz
250:    Successfully saved as D:/Desktop/HBP\250.nii.gz
251:    Successfully saved as D:/Desktop/HBP\251.nii.gz
252:    Successfully saved as D:/Desktop/HBP\252.nii.gz
253:    Successfully saved as D:/Desktop/HBP\253.nii.gz
255:    Successfully saved as D:/Desktop/HBP\255.nii.gz
257:    Successfully saved as D:/Desktop/HBP\257.nii.gz
258:    Successfully saved as D:/Desktop/HBP\258.nii.gz
259:    Successfully saved as D:/Desktop/HBP\259.nii.gz
260:    Successfully saved as D:/Desktop/HBP\260.nii.gz
262:    Successfully saved as D:/Desktop/HBP\262.nii.gz
263:    Successfully saved as D:/Desktop/HBP\263.nii.gz
265:    Successfully saved as D:/Desktop/HBP\265.nii.gz
266:    Successfully saved as D:/Desktop/HBP\266.nii.gz
267:    Successfully saved as D:/Desktop/HBP\267.nii.gz
268:    Successfully saved as D:/Desktop/HBP\268.nii.gz
269:    Successfully saved as D:/Desktop/HBP\269.nii.gz
270:    Successfully saved as D:/Desktop/HBP\270.nii.gz
272:    Successfully saved as D:/Desktop/HBP\272.nii.gz
273:    Successfully saved as D:/Desktop/HBP\273.nii.gz
274:    Successfully saved as D:/Desktop/HBP\274.nii.gz
276:    Successfully saved as D:/Desktop/HBP\276.nii.gz
277:    Successfully saved as D:/Desktop/HBP\277.nii.gz
279:    Successfully saved as D:/Desktop/HBP\279.nii.gz
280:    Successfully saved as D:/Desktop/HBP\280.nii.gz
281:    Successfully saved as D:/Desktop/HBP\281.nii.gz
283:    Successfully saved as D:/Desktop/HBP\283.nii.gz
284:    Successfully saved as D:/Desktop/HBP\284.nii.gz
285:    Successfully saved as D:/Desktop/HBP\285.nii.gz
286:    Successfully saved as D:/Desktop/HBP\286.nii.gz
287:    Successfully saved as D:/Desktop/HBP\287.nii.gz
288:    Successfully saved as D:/Desktop/HBP\288.nii.gz
289:    Successfully saved as D:/Desktop/HBP\289.nii.gz
290:    Successfully saved as D:/Desktop/HBP\290.nii.gz
291:    Successfully saved as D:/Desktop/HBP\291.nii.gz
292:    Successfully saved as D:/Desktop/HBP\292.nii.gz
293:    Successfully saved as D:/Desktop/HBP\293.nii.gz
294:    Successfully saved as D:/Desktop/HBP\294.nii.gz
295:    Successfully saved as D:/Desktop/HBP\295.nii.gz
296:    Successfully saved as D:/Desktop/HBP\296.nii.gz
297:    Successfully saved as D:/Desktop/HBP\297.nii.gz
298:    Successfully saved as D:/Desktop/HBP\298.nii.gz
300:    Successfully saved as D:/Desktop/HBP\300.nii.gz
302:    Successfully saved as D:/Desktop/HBP\302.nii.gz
303:    Successfully saved as D:/Desktop/HBP\303.nii.gz
304:    Successfully saved as D:/Desktop/HBP\304.nii.gz
305:    Successfully saved as D:/Desktop/HBP\305.nii.gz
309:    Successfully saved as D:/Desktop/HBP\309.nii.gz
311:    Successfully saved as D:/Desktop/HBP\311.nii.gz
314:    Successfully saved as D:/Desktop/HBP\314.nii.gz
315:    Successfully saved as D:/Desktop/HBP\315.nii.gz
316:    Successfully saved as D:/Desktop/HBP\316.nii.gz
318:    Successfully saved as D:/Desktop/HBP\318.nii.gz
319:    Successfully saved as D:/Desktop/HBP\319.nii.gz
320:    Successfully saved as D:/Desktop/HBP\320.nii.gz
321:    Successfully saved as D:/Desktop/HBP\321.nii.gz
322:    Successfully saved as D:/Desktop/HBP\322.nii.gz
323:    Successfully saved as D:/Desktop/HBP\323.nii.gz
324:    Successfully saved as D:/Desktop/HBP\324.nii.gz
326:    Successfully saved as D:/Desktop/HBP\326.nii.gz
327:    Successfully saved as D:/Desktop/HBP\327.nii.gz
328:    Successfully saved as D:/Desktop/HBP\328.nii.gz
329:    Successfully saved as D:/Desktop/HBP\329.nii.gz
330:    Successfully saved as D:/Desktop/HBP\330.nii.gz
331:    Successfully saved as D:/Desktop/HBP\331.nii.gz
332:    Successfully saved as D:/Desktop/HBP\332.nii.gz
333:    Successfully saved as D:/Desktop/HBP\333.nii.gz
334:    Successfully saved as D:/Desktop/HBP\334.nii.gz
335:    Successfully saved as D:/Desktop/HBP\335.nii.gz
336:    Successfully saved as D:/Desktop/HBP\336.nii.gz
337:    Successfully saved as D:/Desktop/HBP\337.nii.gz
338:    Successfully saved as D:/Desktop/HBP\338.nii.gz
339:    Successfully saved as D:/Desktop/HBP\339.nii.gz
340:    Successfully saved as D:/Desktop/HBP\340.nii.gz
341:    Successfully saved as D:/Desktop/HBP\341.nii.gz
342:    Successfully saved as D:/Desktop/HBP\342.nii.gz
343:    Successfully saved as D:/Desktop/HBP\343.nii.gz
345:    Successfully saved as D:/Desktop/HBP\345.nii.gz
347:    Successfully saved as D:/Desktop/HBP\347.nii.gz
348:    Successfully saved as D:/Desktop/HBP\348.nii.gz
349:    Successfully saved as D:/Desktop/HBP\349.nii.gz
350:    Successfully saved as D:/Desktop/HBP\350.nii.gz
351:    Successfully saved as D:/Desktop/HBP\351.nii.gz
352:    Successfully saved as D:/Desktop/HBP\352.nii.gz
355:    Successfully saved as D:/Desktop/HBP\355.nii.gz
"""