import pylab as plt
from matplotlib.ticker import ScalarFormatter

pre_500 = [
    (12, [
        (0.1, [1.9891085624694824, 11.133748626708984, 3.2088801860809326]),
        (0.5, [0.20313940048217774, 0.7957747936248779, 0.5027880191802978]),
        (1.0, [0.11725459098815919, 0.4845131874084473, 0.17462539672851562])
    ]),
    (10, [
        (0.1, [1.3734626293182373, 8.387654781341553, 2.5257505893707277]),
        (0.5, [0.25553021430969236, 0.7466716289520263, 0.36412820816040037]),
        (1.0, [0.10543699264526367, 0.3470441818237305, 0.16670730113983154]) # last one interpolated (8+12/2 cores)
    ]),
    (8, [
        (0.1, [1.0158979892730713, 3.2296453952789306, 1.2309767723083496]),
        (0.5, [0.18124637603759766, 0.6300450325012207, 0.25419440269470217]),
        (1.0, [0.10446720123291016, 0.35237441062927244, 0.15878920555114745])
    ]),
    (6, [
        (0.1, [0.9050074100494385, 2.8046098232269285, 1.4134894371032716]),
        (0.5, [0.16694059371948242, 0.5260166168212891, 0.24869179725646973]),
        (1.0, [0.09754080772399902, 0.2983243942260742, 0.1566009998321533])
    ]),
    (4, [
        (0.1, [0.9945375919342041, 2.569732999801636, 1.7039597988128663]),
        (0.5, [0.1824036121368408, 0.48777003288269044, 0.25487580299377444]),
        (1.0, [0.0851017951965332, 0.2620424270629883, 0.15948376655578614])
    ]),
    (2, [
        (0.1, [1.985216999053955, 2.574205017089844, 1.728466844558716]),
        (0.5, [0.19835081100463867, 0.5193762302398681, 0.3593235969543457]),
        (1.0, [0.10628962516784668, 0.2781211853027344, 0.19967761039733886])
    ]),
    (1, [
        (0.1, [1.366194200515747, 2.9491868019104004, 2.8753024101257325]),
        (0.5, [0.28014678955078126, 0.6240676403045654, 0.6062560081481934]),
        (1.0, [0.14880080223083497, 0.32180280685424806, 0.31407480239868163])
    ]),
]

pre_1000 = [
    (12, [
        (0.1, [3.9923954010009766, 23.813285398483277, 13.20119242668152]),
        (0.5, [0.3263136386871338, 1.4725118160247803, 0.5621849536895752]),
        (1.0, [0.17148299217224122, 2.256487560272217, 0.3898597717285156])
    ]),
    (10, [
        (0.1, [3.000665378570557, 6.947900199890137, 2.3990228176116943]),
        (0.5, [0.37705378532409667, 1.3704967975616456, 0.6241794109344483]),
        (1.0, [0.1729748249053955, 0.7025846004486084, 0.23936519622802735])
    ]),
    (8, [
        (0.1, [2.6253734111785887, 5.736714601516724, 2.358508014678955]),
        (0.5, [0.3159488201141357, 1.2668225765228271, 0.4820581912994385]),
        (1.0, [0.16247401237487794, 0.6817934036254882, 0.3004568099975586])
    ]),
    (6, [
        (0.1, [1.3526776313781739, 5.121266174316406, 2.4254594326019285]),
        (0.5, [0.2960458278656006, 1.0713375568389893, 0.47456722259521483]),
        (1.0, [0.15409259796142577, 0.5804428100585938, 0.2618733882904053])
    ]),
    (4, [
        (0.1, [1.3510666370391846, 4.853658390045166, 2.2391282081604005]),
        (0.5, [0.2762184143066406, 0.9506045818328858, 0.45893683433532717]),
        (1.0, [0.1393350124359131, 0.49213299751281736, 0.2534604072570801])
    ]),
    (2, [
        (0.1, [1.9199141979217529, 4.818789005279541, 3.2025725841522217]),
        (0.5, [0.33088197708129885, 1.0134772300720214, 0.6722692012786865]),
        (1.0, [0.17750897407531738, 0.5182333946228027, 0.35013580322265625])
    ]),
    (1, [
        (0.1, [2.500531768798828, 5.6564216136932375, 5.4056031703948975]),
        (0.5, [0.5011705875396728, 1.1466609954833984, 1.088066005706787]),
        (1.0, [0.25618977546691896, 0.5961260318756103, 0.591838788986206])
    ]),
]

pre_2000 = [
    (12, [
        (0.1, [5.044118022918701, 21.7452663898468, 15.287217998504639]),
        (0.5, [0.6411756038665771, 3.392827558517456, 0.9674943923950196]),
        (1.0, [0.32332763671875, 1.6466599941253661, 1.716783380508423])
    ]),
    (10, [
        (0.1, [3.3319177627563477, 15.268317413330077, 5.610977602005005]),
        (0.5, [0.7326796054840088, 3.018211603164673, 0.921956205368042]),
        (1.0, [0.3114037990570068, 1.3452052116394042, 0.5280020236968994])
    ]),
    (8, [
        (0.1, [2.808287191390991, 11.61716341972351, 4.779117822647095]),
        (0.5, [0.5653376102447509, 2.423179578781128, 0.9161164283752441]),
        (1.0, [0.3176270008087158, 1.2210777759552003, 0.40888419151306155])
    ]),
    (6, [
        (0.1, [2.449811029434204, 10.347668790817261, 4.034867429733277]),
        (0.5, [0.5510233879089356, 1.9718682289123535, 0.7801834106445312]),
        (1.0, [0.26662502288818357, 1.0652428150177002, 0.4563755989074707])
    ]),
    (4, [
        (0.1, [2.8192188262939455, 8.985540199279786, 4.618443584442138]),
        (0.5, [0.4862639904022217, 1.9207717895507812, 0.8529573917388916]),
        (1.0, [0.25661120414733884, 0.9705232143402099, 0.4834399700164795])
    ]),
    (2, [
        (0.1, [3.298360586166382, 9.421814012527467, 6.39957857131958]),
        (0.5, [0.6278913974761963, 1.9614768028259277, 1.2657363891601563]),
        (1.0, [0.31787919998168945, 1.0087130069732666, 0.6979300022125244])
    ]),
    (1, [
        (0.1, [4.624171161651612, 10.751064205169678, 10.527126598358155]),
        (0.5, [0.9229228019714355, 2.2314202308654787, 2.173206996917725]),
        (1.0, [0.4722142219543457, 1.1528783798217774, 1.1420582294464112])
    ]),
]
cores = [12, 10, 8, 6, 4, 2, 1]


plt.figure()
plt.suptitle("Connection types at 1s duration/0.1ms resolution", size = 14)
plt.subplots_adjust(hspace = 0.1)

ax = plt.subplot(311)
plt.text(0.5, 0.85, "500 neurons", horizontalalignment = 'center', transform = ax.transAxes)
plt.plot(cores, [x[1][0][1][0] for x in pre_500], "b", label = 'static')
plt.plot(cores, [x[1][0][1][1] for x in pre_500], "r", label = 'standard')
plt.plot(cores, [x[1][0][1][2] for x in pre_500], "g", label = 'STDPNode')
plt.ylabel("Time (s)")
plt.xlim(0, 13)
plt.xticks(cores, [])
plt.legend(loc = "upper center", frameon = False, ncol = 3, bbox_to_anchor = (0.5, 1.28), prop = { 'size': 13 })

ax = plt.subplot(312)
plt.text(0.5, 0.85, "1'000 neurons", horizontalalignment = 'center', transform = ax.transAxes)
plt.plot(cores, [x[1][0][1][0] for x in pre_1000], "b")
plt.plot(cores, [x[1][0][1][1] for x in pre_1000], "r")
plt.plot(cores, [x[1][0][1][2] for x in pre_1000], "g")
plt.ylabel("Time (s)")
plt.xlim(0, 13)
plt.xticks(cores, [])

ax = plt.subplot(313)
plt.text(0.5, 0.85, "2'000 neurons", horizontalalignment = 'center', transform = ax.transAxes)
plt.plot(cores, [x[1][0][1][0] for x in pre_2000], "b", label = 'static')
plt.plot(cores, [x[1][0][1][1] for x in pre_2000], "r", label = 'standard')
plt.plot(cores, [x[1][0][1][2] for x in pre_2000], "g", label = 'STDPNode')
plt.xlabel("Cores")
plt.ylabel("Time (s)")
plt.xlim(0, 13)
plt.xticks(cores)


plt.figure()
plt.suptitle("Connection types at 1s duration/0.5ms resolution", size = 14)
plt.subplots_adjust(hspace = 0.1)

ax = plt.subplot(311)
plt.text(0.5, 0.85, "500 neurons", horizontalalignment = 'center', transform = ax.transAxes)
plt.plot(cores, [x[1][1][1][0] for x in pre_500], "b", label = 'static')
plt.plot(cores, [x[1][1][1][1] for x in pre_500], "r", label = 'standard')
plt.plot(cores, [x[1][1][1][2] for x in pre_500], "g", label = 'STDPNode')
plt.ylabel("Time (s)")
plt.xlim(0, 13)
plt.xticks(cores, [])
plt.legend(loc = "upper center", frameon = False, ncol = 3, bbox_to_anchor = (0.5, 1.28), prop = { 'size': 13 })

ax = plt.subplot(312)
plt.text(0.5, 0.85, "1'000 neurons", horizontalalignment = 'center', transform = ax.transAxes)
plt.plot(cores, [x[1][1][1][0] for x in pre_1000], "b")
plt.plot(cores, [x[1][1][1][1] for x in pre_1000], "r")
plt.plot(cores, [x[1][1][1][2] for x in pre_1000], "g")
plt.ylabel("Time (s)")
plt.xlim(0, 13)
plt.xticks(cores, [])

ax = plt.subplot(313)
plt.text(0.5, 0.85, "2'000 neurons", horizontalalignment = 'center', transform = ax.transAxes)
plt.plot(cores, [x[1][1][1][0] for x in pre_2000], "b", label = 'static')
plt.plot(cores, [x[1][1][1][1] for x in pre_2000], "r", label = 'standard')
plt.plot(cores, [x[1][1][1][2] for x in pre_2000], "g", label = 'STDPNode')
plt.xlabel("Cores")
plt.ylabel("Time (s)")
plt.xlim(0, 13)
plt.xticks(cores)


plt.figure()
plt.suptitle("Connection types at 1s duration/1ms resolution", size = 14)
plt.subplots_adjust(hspace = 0.1)

ax = plt.subplot(311)
plt.text(0.5, 0.85, "500 neurons", horizontalalignment = 'center', transform = ax.transAxes)
plt.plot(cores, [x[1][2][1][0] for x in pre_500], "b", label = 'static')
plt.plot(cores, [x[1][2][1][1] for x in pre_500], "r", label = 'standard')
plt.plot(cores, [x[1][2][1][2] for x in pre_500], "g", label = 'STDPNode')
plt.ylabel("Time (s)")
plt.xlim(0, 13)
plt.xticks(cores, [])
plt.legend(loc = "upper center", frameon = False, ncol = 3, bbox_to_anchor = (0.5, 1.28), prop = { 'size': 13 })

ax = plt.subplot(312)
plt.text(0.5, 0.85, "1'000 neurons", horizontalalignment = 'center', transform = ax.transAxes)
plt.plot(cores, [x[1][2][1][0] for x in pre_1000], "b")
plt.plot(cores, [x[1][2][1][1] for x in pre_1000], "r")
plt.plot(cores, [x[1][2][1][2] for x in pre_1000], "g")
plt.ylabel("Time (s)")
plt.xlim(0, 13)
plt.xticks(cores, [])

ax = plt.subplot(313)
plt.text(0.5, 0.85, "2'000 neurons", horizontalalignment = 'center', transform = ax.transAxes)
plt.plot(cores, [x[1][2][1][0] for x in pre_2000], "b", label = 'static')
plt.plot(cores, [x[1][2][1][1] for x in pre_2000], "r", label = 'standard')
plt.plot(cores, [x[1][2][1][2] for x in pre_2000], "g", label = 'STDPNode')
plt.xlabel("Cores")
plt.ylabel("Time (s)")
plt.xlim(0, 13)
plt.xticks(cores)

plt.show()
