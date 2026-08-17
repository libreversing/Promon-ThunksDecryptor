import re

# very lazy behavior, no need to have exactly same format as me
# just copy paste and it works, if it doesn't please send an issue with the qword table and the script so i can fix it
table = """
__data:0000000000A40100 8C BA A9 84 qword_A40100    DCQ 0xAB67604284A9BA8C  ; DATA XREF: sub_8C567C+49EC↑o
__data:0000000000A40100 42 60 67 AB                                         ; sub_8C567C+C080↑o ...
__data:0000000000A40108 8C EC 00 09 qword_A40108    DCQ 0x56CEC0850900EC8C  ; DATA XREF: sub_969D7C↑o
__data:0000000000A40108 85 C0 CE 56                                         ; sub_969D7C+4↑r
__data:0000000000A40110 7C A8 30 8D qword_A40110    DCQ 0x23620C78D30A87C   ; DATA XREF: sub_969B18↑o
__data:0000000000A40110 C7 20 36 02                                         ; sub_969B18+4↑r
__data:0000000000A40118 AC 6E 05 11 qword_A40118    DCQ 0xAD9D810A11056EAC  ; DATA XREF: sub_96944C↑o
__data:0000000000A40118 0A 81 9D AD                                         ; sub_96944C+4↑r
__data:0000000000A40120 1C 22 A3 95 qword_A40120    DCQ 0x5904E14C95A3221C  ; DATA XREF: sub_969488↑o
__data:0000000000A40120 4C E1 04 59                                         ; sub_969488+4↑r
__data:0000000000A40128 A4 53 B5 19 qword_A40128    DCQ 0x46C418F19B553A4   ; DATA XREF: sub_969DDC↑o
__data:0000000000A40128 8F 41 6C 04                                         ; sub_969DDC+4↑r
__data:0000000000A40130             ; __int64 (*qword_A40130)(void)
__data:0000000000A40130 4C 9E FC 9D qword_A40130    DCQ 0xAFD3A1D19DFC9E4C  ; DATA XREF: sub_969674↑o
__data:0000000000A40130 D1 A1 D3 AF                                         ; sub_969674+4↑r
__data:0000000000A40138 58 AA 56 22 qword_A40138    DCQ 0x5B3B02142256AA58  ; DATA XREF: sub_969644↑o
__data:0000000000A40138 14 02 3B 5B                                         ; sub_969644+4↑r
__data:0000000000A40140 88 B4 8C A6 qword_A40140    DCQ 0x6A26256A68CB488   ; DATA XREF: sub_969E90↑o
__data:0000000000A40140 56 62 A2 06                                         ; sub_969E90+4↑r
__data:0000000000A40148             ; __int64 (*qword_A40148)(void)
__data:0000000000A40148 AC 5B C4 2A qword_A40148    DCQ 0xB209C2992AC45BAC  ; DATA XREF: sub_9690E0↑o
__data:0000000000A40148 99 C2 09 B2                                         ; sub_9690E0+4↑r
__data:0000000000A40150             ; __int64 (*qword_A40150)(void)
__data:0000000000A40150 74 FB 22 AF qword_A40150    DCQ 0x5D7122DBAF22FB74  ; DATA XREF: sub_9694AC↑o
__data:0000000000A40150 DB 22 71 5D                                         ; sub_9694AC+4↑r
__data:0000000000A40158 7C F5 D5 32 qword_A40158    DCQ 0x8D8831E32D5F57C   ; DATA XREF: sub_969848↑o
__data:0000000000A40158 1E 83 D8 08                                         ; sub_969848+4↑r
__data:0000000000A40160 E4 94 12 B7 qword_A40160    DCQ 0xB43FE360B71294E4  ; DATA XREF: sub_969614↑o
__data:0000000000A40160 60 E3 3F B4                                         ; sub_969614+4↑r
__data:0000000000A40168 64 05 7F 3B qword_A40168    DCQ 0x5FA743A33B7F0564  ; DATA XREF: sub_969C2C↑o
__data:0000000000A40168 A3 43 A7 5F                                         ; sub_969C2C+4↑r
__data:0000000000A40170             ; __int64 (*qword_A40170)(void)
__data:0000000000A40170 90 B6 96 BF qword_A40170    DCQ 0xB0EA3E5BF96B690   ; DATA XREF: sub_969DA0↑o
__data:0000000000A40170 E5 A3 0E 0B                                         ; sub_969DA0+4↑r
__data:0000000000A40178 64 4B 34 44 qword_A40178    DCQ 0xB676042844344B64  ; DATA XREF: sub_9696BC↑o
__data:0000000000A40178 28 04 76 B6                                         ; sub_9696BC+4↑r
__data:0000000000A40180 88 51 82 C8 qword_A40180    DCQ 0x61DD646AC8825188  ; DATA XREF: sub_969014↑o
__data:0000000000A40180 6A 64 DD 61                                         ; sub_969014+4↑r
__data:0000000000A40188 70 49 A2 4C qword_A40188    DCQ 0xD44C4AD4CA24970   ; DATA XREF: sub_969BB4↑o
__data:0000000000A40188 AD C4 44 0D                                         ; sub_969BB4+4↑r
__data:0000000000A40190 68 F9 D4 D0 qword_A40190    DCQ 0xB8AC24EFD0D4F968  ; DATA XREF: sub_969B78↑o
__data:0000000000A40190 EF 24 AC B8                                         ; sub_969B78+4↑r
__data:0000000000A40198             ; __int64 (*qword_A40198)(void)
__data:0000000000A40198 24 75 17 55 qword_A40198    DCQ 0x6413853255177524  ; DATA XREF: sub_969620↑o
__data:0000000000A40198 32 85 13 64                                         ; sub_969620+4↑r
__data:0000000000A401A0 38 63 7C D9 qword_A401A0    DCQ 0xF7AE574D97C6338   ; DATA XREF: sub_969A1C↑o
__data:0000000000A401A0 74 E5 7A 0F                                         ; sub_969A1C+4↑r
__data:0000000000A401A8 3C 40 2C 5D qword_A401A8    DCQ 0xBAE245B75D2C403C  ; DATA XREF: sub_969E9C↑o
__data:0000000000A401A8 B7 45 E2 BA                                         ; sub_969E9C+4↑r
__data:0000000000A401B0 30 9D EE E1 qword_A401B0    DCQ 0x6649A5F9E1EE9D30  ; DATA XREF: sub_969518↑o
__data:0000000000A401B0 F9 A5 49 66                                         ; sub_969518+4↑r
__data:0000000000A401B8 50 CF 2E 66 qword_A401B8    DCQ 0x11B1063C662ECF50  ; DATA XREF: sub_969B84↑o
__data:0000000000A401B8 3C 06 B1 11                                         ; sub_969B84+4↑r
__data:0000000000A401C0 B4 3E 44 EA qword_A401C0    DCQ 0xBD18667EEA443EB4  ; DATA XREF: sub_969530↑o
__data:0000000000A401C0 7E 66 18 BD                                         ; sub_969530+4↑r
__data:0000000000A401C8 48 1D 84 6E qword_A401C8    DCQ 0x687FC6C16E841D48  ; DATA XREF: sub_969590↑o
__data:0000000000A401C8 C1 C6 7F 68                                         ; sub_969590+4↑r
__data:0000000000A401D0 B8 E2 D7 F2 qword_A401D0    DCQ 0x13E72703F2D7E2B8  ; DATA XREF: sub_96902C↑o
__data:0000000000A401D0 03 27 E7 13                                         ; sub_96902C+4↑r
__data:0000000000A401D8 B0 9E FF 76 qword_A401D8    DCQ 0xBF4E874676FF9EB0  ; DATA XREF: sub_969E78↑o
__data:0000000000A401D8 46 87 4E BF                                         ; sub_969E78+4↑r
__data:0000000000A401E0             ; __int64 (*qword_A401E0)(void)
__data:0000000000A401E0 24 D6 37 FB qword_A401E0    DCQ 0x6AB5E788FB37D624  ; DATA XREF: import__syscall4↑o
__data:0000000000A401E0 88 E7 B5 6A                                         ; import__syscall4+4↑r
__data:0000000000A401E8 10 23 96 7F qword_A401E8    DCQ 0x161D47CB7F962310  ; DATA XREF: sub_969B9C↑o
__data:0000000000A401E8 CB 47 1D 16                                         ; sub_969B9C+4↑r
__data:0000000000A401F0 A4 B9 CE 03 qword_A401F0    DCQ 0xC184A80E03CEB9A4  ; DATA XREF: sub_969DF4↑o
__data:0000000000A401F0 0E A8 84 C1                                         ; sub_969DF4+4↑r
__data:0000000000A401F8 BC 64 EC 87 qword_A401F8    DCQ 0x6CEC085087EC64BC  ; DATA XREF: sub_969E60↑o
__data:0000000000A401F8 50 08 EC 6C                                         ; sub_969E60+4↑r
__data:0000000000A40200 68 2E 44 0C qword_A40200    DCQ 0x185368930C442E68  ; DATA XREF: sub_9699EC↑o
__data:0000000000A40200 93 68 53 18                                         ; sub_9699EC+4↑r
__data:0000000000A40208 E0 6F 84 90 qword_A40208    DCQ 0xC3BAC8D590846FE0  ; DATA XREF: sub_969C14↑o
__data:0000000000A40208 D5 C8 BA C3                                         ; sub_969C14+4↑r
__data:0000000000A40210 B0 FF BC 14 qword_A40210    DCQ 0x6F22291814BCFFB0  ; DATA XREF: sub_969DD0↑o
__data:0000000000A40210 18 29 22 6F                                         ; sub_969DD0+4↑r
__data:0000000000A40218 A8 14 CE 98 qword_A40218    DCQ 0x1A89895A98CE14A8  ; DATA XREF: sub_9693E0↑o
__data:0000000000A40218 5A 89 89 1A                                         ; sub_9693E0+4↑r
__data:0000000000A40220 0C C7 B7 1C qword_A40220    DCQ 0xC5F0E99D1CB7C70C  ; DATA XREF: sub_96917C↑o
__data:0000000000A40220 9D E9 F0 C5                                         ; sub_96917C+4↑r
__data:0000000000A40228 E4 ED 5B A1 qword_A40228    DCQ 0x715849DFA15BEDE4  ; DATA XREF: sub_969EC0↑o
__data:0000000000A40228 DF 49 58 71                                         ; sub_969EC0+4↑r
__data:0000000000A40230 74 4A 32 25 qword_A40230    DCQ 0x1CBFAA2225324A74  ; DATA XREF: sub_969C20↑o
__data:0000000000A40230 22 AA BF 1C                                         ; sub_969C20+4↑r
__data:0000000000A40238 04 6C D6 A9 qword_A40238    DCQ 0xC8270A64A9D66C04  ; DATA XREF: sub_96920C↑o
__data:0000000000A40238 64 0A 27 C8                                         ; sub_96920C+4↑r
__data:0000000000A40240 B8 86 1C 2E qword_A40240    DCQ 0x738E6AA72E1C86B8  ; DATA XREF: sub_969C38↑o
__data:0000000000A40240 A7 6A 8E 73                                         ; sub_969C38+4↑r
__data:0000000000A40248 98 1D DA B1 qword_A40248    DCQ 0x1EF5CAE9B1DA1D98  ; DATA XREF: sub_969DE8↑o
__data:0000000000A40248 E9 CA F5 1E                                         ; sub_969DE8+4↑r
__data:0000000000A40250 C0 10 A0 36 qword_A40250    DCQ 0xCA5D2B2C36A010C0  ; DATA XREF: sub_969A4C↑o
__data:0000000000A40250 2C 2B 5D CA                                         ; sub_969A4C+4↑r
__data:0000000000A40258 9C C2 C4 BA qword_A40258    DCQ 0x75C48B6EBAC4C29C  ; DATA XREF: sub_9696B0↑o
__data:0000000000A40258 6E 8B C4 75                                         ; sub_9696B0+4↑r
__data:0000000000A40260 94 DB 92 3E qword_A40260    DCQ 0x212BEBB13E92DB94  ; DATA XREF: sub_969D94↑o
__data:0000000000A40260 B1 EB 2B 21                                         ; sub_969D94+4↑r
__data:0000000000A40268             ; __int64 (*qword_A40268)(void)
__data:0000000000A40268 08 0F 2F C3 qword_A40268    DCQ 0xCC934BF3C32F0F08  ; DATA XREF: sub_96962C↑o
__data:0000000000A40268 F3 4B 93 CC                                         ; sub_96962C+4↑r
__data:0000000000A40270 A0 82 47 47 qword_A40270    DCQ 0x77FAAC36474782A0  ; DATA XREF: sub_969DC4↑o
__data:0000000000A40270 36 AC FA 77                                         ; sub_969DC4+4↑r
__data:0000000000A40278 A8 EE 99 CB qword_A40278    DCQ 0x23620C78CB99EEA8  ; DATA XREF: sub_969C08↑o
__data:0000000000A40278 78 0C 62 23                                         ; sub_969C08+4↑r
__data:0000000000A40280 C0 5B DF 4F qword_A40280    DCQ 0xCEC96CBB4FDF5BC0  ; DATA XREF: sub_969038↑o
__data:0000000000A40280 BB 6C C9 CE                                         ; sub_969038+4↑r
__data:0000000000A40288             ; __int64 (*qword_A40288)(void)
__data:0000000000A40288 60 27 1B D4 qword_A40288    DCQ 0x7A30CCFDD41B2760  ; DATA XREF: sub_96947C↑o
__data:0000000000A40288 FD CC 30 7A                                         ; sub_96947C+4↑r
__data:0000000000A40290 7C 63 4D 58 qword_A40290    DCQ 0x25982D40584D637C  ; DATA XREF: sub_969E84↑o
__data:0000000000A40290 40 2D 98 25                                         ; sub_969E84+4↑r
__data:0000000000A40298 F8 9D B8 DC qword_A40298    DCQ 0xD0FF8D82DCB89DF8  ; DATA XREF: sub_969C44↑o
__data:0000000000A40298 82 8D FF D0                                         ; sub_969C44+4↑r
__data:0000000000A402A0             ; __int64 (*qword_A402A0)(void)
__data:0000000000A402A0 48 02 EA 60 qword_A402A0    DCQ 0x7C66EDC560EA0248  ; DATA XREF: sub_9690B0↑o
__data:0000000000A402A0 C5 ED 66 7C                                         ; sub_9690B0+4↑r
__data:0000000000A402A8 B4 A2 D9 E4 qword_A402A8    DCQ 0x27CE4E07E4D9A2B4  ; DATA XREF: sub_969E3C↑o
__data:0000000000A402A8 07 4E CE 27                                         ; sub_969E3C+4↑r
__data:0000000000A402B0 08 FC 16 69 qword_A402B0    DCQ 0xD335AE4A6916FC08  ; DATA XREF: sub_969C8C↑o
__data:0000000000A402B0 4A AE 35 D3                                         ; sub_969C8C+4↑r
__data:0000000000A402B8             ; __int64 (*qword_A402B8)(void)
__data:0000000000A402B8 5C A2 28 ED qword_A402B8    DCQ 0x7E9D0E8CED28A25C  ; DATA XREF: sub_969FC8↑o
__data:0000000000A402B8 8C 0E 9D 7E                                         ; sub_969FC8+4↑r
__data:0000000000A402C0 74 15 C1 71 qword_A402C0    DCQ 0x2A046ECF71C11574  ; DATA XREF: sub_969B90↑o
__data:0000000000A402C0 CF 6E 04 2A                                         ; sub_969B90+4↑r
__data:0000000000A402C8 B8 A7 F6 F5 qword_A402C8    DCQ 0xD56BCF11F5F6A7B8  ; DATA XREF: sub_969C68↑o
__data:0000000000A402C8 11 CF 6B D5                                         ; sub_969C68+4↑r
__data:0000000000A402D0 D8 28 4C 7A qword_A402D0    DCQ 0x80D32F547A4C28D8  ; DATA XREF: sub_969110↑o
__data:0000000000A402D0 54 2F D3 80                                         ; sub_969110+4↑r
__data:0000000000A402D8 C4 67 50 FE qword_A402D8    DCQ 0x2C3A8F96FE5067C4  ; DATA XREF: sub_9695B4↑o
__data:0000000000A402D8 96 8F 3A 2C                                         ; sub_9695B4+4↑r
__data:0000000000A402E0             ; __int64 (*qword_A402E0)(void)
__data:0000000000A402E0 40 DE D1 82 qword_A402E0    DCQ 0xD7A1EFD982D1DE40  ; DATA XREF: sub_969BCC↑o
__data:0000000000A402E0 D9 EF A1 D7                                         ; sub_969BCC+4↑r
__data:0000000000A402E8             ; __int64 (*qword_A402E8)(void)
__data:0000000000A402E8 0C A0 F5 06 qword_A402E8    DCQ 0x8309501C06F5A00C  ; DATA XREF: sub_969224↑o
__data:0000000000A402E8 1C 50 09 83                                         ; sub_969224+4↑r
__data:0000000000A402F0 34 1D 0E 8B qword_A402F0    DCQ 0x2E70B05E8B0E1D34  ; DATA XREF: sub_969AC4↑o
__data:0000000000A402F0 5E B0 70 2E                                         ; sub_969AC4+4↑r
__data:0000000000A402F8 1C EE 6F 0F qword_A402F8    DCQ 0xD9D810A10F6FEE1C  ; DATA XREF: sub_969470↑o
__data:0000000000A402F8 A1 10 D8 D9                                         ; sub_969470+4↑r
__data:0000000000A40300 54 93 6C 93 qword_A40300    DCQ 0x853F70E3936C9354  ; DATA XREF: sub_9697C4↑o
__data:0000000000A40300 E3 70 3F 85                                         ; sub_9697C4+4↑r
__data:0000000000A40308 08 72 C2 17 qword_A40308    DCQ 0x30A6D12617C27208  ; DATA XREF: sub_9694B8↑o
__data:0000000000A40308 26 D1 A6 30                                         ; sub_9694B8+4↑r
__data:0000000000A40310 D8 05 3A 9C qword_A40310    DCQ 0xDC0E31689C3A05D8  ; DATA XREF: sub_96911C↑o
__data:0000000000A40310 68 31 0E DC                                         ; sub_96911C+4↑r
__data:0000000000A40318 1C 0B 35 20 qword_A40318    DCQ 0x877591AB20350B1C  ; DATA XREF: sub_969434↑o
__data:0000000000A40318 AB 91 75 87                                         ; sub_969434+4↑r
__data:0000000000A40320 3C 9C 5B A4 qword_A40320    DCQ 0x32DCF1EDA45B9C3C  ; DATA XREF: sub_969698↑o
__data:0000000000A40320 ED F1 DC 32                                         ; sub_969698+4↑r"""

matches = re.findall(r"([0-9A-Fa-f]{8,16}).*?DCQ\s+(0x[0-9A-Fa-f]+)", table) # yes, very lazy 
decryption_key = 0xAB676042843BC1B0

for i, (addr, val) in enumerate(matches):
    decrypted = hex((int(val, 16) - (i + 1) * decryption_key) & 0xFFFFFFFFFFFFFFFF) # decryption here
    print(f"[{i}][{addr}][{val}] Decypted Address: {decrypted}")