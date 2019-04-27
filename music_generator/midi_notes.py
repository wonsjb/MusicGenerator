class Item:
    def __init__(self, midi, organ, piano, english, german, frequency):
        self.midi = midi
        self.organ = organ
        self.piano = piano
        self.english = english
        self.german = german
        self.frequency = frequency


data = [
    Item(127, None, None, "G9", "g’’’’’’", 12543.85),
    Item(126, None, None, "F#9/Gb9", "fis’’’’’’/ges’’’’’’", 11839.82),
    Item(125, None, None, "F9", "f’’’’’’", 11175.30),
    Item(124, None, None, "E9", "e’’’’’’", 10548.08),
    Item(123, None, None, "D#9/Eb9", "dis’’’’’’/es’’’’’’", 9956.06),
    Item(122, None, None, "D9", "d’’’’’’", 9397.27),
    Item(121, None, None, "C#9/Db9", "cis’’’’’’/des’’’’’’", 8869.84),
    Item(120, None, None, "C9", "c’’’’’’", 8372.02),
    Item(119, None, None, "B8", "h’’’’’", 7902.13),
    Item(118, None, None, "A#8/Bb8", "ais’’’’’/b’’’’’", 7458.62),
    Item(117, None, None, "A8", "a’’’’’", 7040.00),
    Item(116, None, None, "G#8/Ab8", "gis’’’’’/ges’’’’’", 6644.88),
    Item(115, None, None, "G8", "g’’’’’", 6271.93),
    Item(114, None, None, "F#8/Gb8", "fis’’’’’/ges’’’’’", 5919.91),
    Item(113, None, None, "F8", "f’’’’’", 5587.65),
    Item(112, None, None, "E8", "e’’’’’", 5274.04),
    Item(111, None, None, "D#8/Eb8", "dis’’’’’/es’’’’’", 4978.03),
    Item(110, None, None, "D8", "d’’’’’", 4698.64),
    Item(109, None, None, "C#8/Db8", "cis’’’’’/des’’’’’", 4434.92),
    Item(108, None, 88, "C8", "c’’’’’", 4186.01),
    Item(107, None, 87, "B7", "h’’’’", 3951.07),
    Item(106, None, 86, "A#7/Bb7", "ais’’’’/b’’’’", 3729.31),
    Item(105, None, 85, "A7", "a’’’’", 3520.00),
    Item(104, None, 84, "G#7/Ab7", "gis’’’’/ges’’’’", 3322.44),
    Item(103, None, 83, "G7", "g’’’’", 3135.96),
    Item(102, None, 82, "F#7/Gb7", "fis’’’’/ges’’’’", 2959.96),
    Item(101, None, 81, "F7", "f’’’’", 2793.83),
    Item(100, None, 80, "E7", "e’’’’", 2637.02),
    Item(99, None, 79, "D#7/Eb7", "dis’’’’/es’’’’", 2489.02),
    Item(98, None, 78, "D7", "d’’’’", 2349.32),
    Item(97, None, 77, "C#7/Db7", "cis’’’’/des’’’’", 2217.46),
    Item(96, 61, 76, "C7", "c’’’’", 2093.00),
    Item(95, 60, 75, "B6", "h’’’", 1975.53),
    Item(94, 59, 74, "A#6/Bb6", "ais’’’/b’’’", 1864.66),
    Item(93, 58, 73, "A6", "a’’’", 1760.00),
    Item(92, 57, 72, "G#6/Ab6", "gis’’’/as’’’", 1661.22),
    Item(91, 56, 71, "G6", "g’’’", 1567.98),
    Item(90, 55, 70, "F#6/Gb6", "fis’’’/ges’’’", 1479.98),
    Item(89, 54, 69, "F6", "f’’’", 1396.91),
    Item(88, 53, 68, "E6", "e’’’", 1318.51),
    Item(87, 52, 67, "D#6/Eb6", "dis’’’/es’’’", 1244.51),
    Item(86, 51, 66, "D6", "d’’’", 1174.66),
    Item(85, 50, 65, "C#6/Db6", "cis’’’/des’’’", 1108.73),
    Item(84, 49, 64, "C6", "c’’’", 1046.50),
    Item(83, 48, 63, "B5", "h’’", 987.77),
    Item(82, 47, 62, "A#5/Bb5", "ais’’/b’’", 932.33),
    Item(81, 46, 61, "A5", "a’’", 880.00),
    Item(80, 45, 60, "G#5/Ab5", "gis’’/as’’", 830.61),
    Item(79, 44, 59, "G5", "g’’", 783.99),
    Item(78, 43, 58, "F#5/Gb5", "fis’’/ges’’", 739.99),
    Item(77, 42, 57, "F5", "f’’", 698.46),
    Item(76, 41, 56, "E5", "e’’", 659.26),
    Item(75, 40, 55, "D#5/Eb5", "dis’’/es’’", 622.25),
    Item(74, 39, 54, "D5", "d’’", 587.33),
    Item(73, 38, 53, "C#5/Db5", "cis’’/des’’", 554.37),
    Item(72, 37, 52, "C5", "c’’", 523.25),
    Item(71, 36, 51, "B4", "h’", 493.88),
    Item(70, 35, 50, "A#4/Bb4", "ais’/b’", 466.16),
    Item(69, 34, 49, "A4concertpitch", "a’Kammerton", 440.00),
    Item(68, 33, 48, "G#4/Ab4", "gis’/as’", 415.30),
    Item(67, 32, 47, "G4", "g’", 392.00),
    Item(66, 31, 46, "F#4/Gb4", "fis’/ges’", 369.99),
    Item(65, 30, 45, "F4", "f’", 349.23),
    Item(64, 29, 44, "E4", "e’", 329.63),
    Item(63, 28, 43, "D#4/Eb4", "dis’/es’", 311.13),
    Item(62, 27, 42, "D4", "d’", 293.66),
    Item(61, 26, 41, "C#4/Db4", "cis’/des’", 277.18),
    Item(60, 25, 40, "C4(middleC)", "c’(Schloss-C)", 261.63),
    Item(59, 24, 39, "B3", "h", 246.94),
    Item(58, 23, 38, "A#3/Bb3", "ais/b", 233.08),
    Item(57, 22, 37, "A3", "a", 220.00),
    Item(56, 21, 36, "G#3/Ab3", "gis/as", 207.65),
    Item(55, 20, 35, "G3", "g", 196.00),
    Item(54, 19, 34, "F#3/Gb3", "fis/ges", 185.00),
    Item(53, 18, 33, "F3", "f", 174.61),
    Item(52, 17, 32, "E3", "e", 164.81),
    Item(51, 16, 31, "D#3/Eb3", "dis/es", 155.56),
    Item(50, 15, 30, "D3", "d", 146.83),
    Item(49, 14, 29, "C#3/Db3", "cis/des", 138.59),
    Item(48, 13, 28, "C3", "c", 130.81),
    Item(47, 12, 27, "B2", "H", 123.47),
    Item(46, 11, 26, "A#2/Bb2", "Ais/B", 116.54),
    Item(45, 10, 25, "A2", "A", 110.00),
    Item(44, 9, 24, "G#2/Ab2", "Gis/As", 103.83),
    Item(43, 8, 23, "G2", "G", 98.00),
    Item(42, 7, 22, "F#2/Gb2", "Fis/Ges", 92.50),
    Item(41, 6, 21, "F2", "F", 87.31),
    Item(40, 5, 20, "E2", "E", 82.41),
    Item(39, 4, 19, "D#2/Eb2", "Dis/Es", 77.78),
    Item(38, 3, 18, "D2", "D", 73.42),
    Item(37, 2, 17, "C#2/Db2", "Cis/Des", 69.30),
    Item(36, 1, 16, "C2", "C", 65.41),
    Item(35, None, 15, "B1", "H1", 61.74),
    Item(34, None, 14, "A#1/Bb1", "Ais1/b1", 58.27),
    Item(33, None, 13, "A1", "A1", 55.00),
    Item(32, None, 12, "G#1/Ab1", "Gis1/As1", 51.91),
    Item(31, None, 11, "G1", "G1", 49.00),
    Item(30, None, 10, "F#1/Gb1", "Fis1/Ges1", 46.25),
    Item(29, None, 9, "F1", "F1", 43.65),
    Item(28, None, 8, "E1", "E1", 41.20),
    Item(27, None, 7, "D#1/Eb1", "Dis1/Es1", 38.89),
    Item(26, None, 6, "D1", "D1", 36.71),
    Item(25, None, 5, "C#1/Db1", "Cis1/Des1", 34.65),
    Item(24, None, 4, "C1", "C1", 32.70),
    Item(23, None, 3, "B0", "H2", 30.87),
    Item(22, None, 2, "A#0/Bb0", "Ais2/B2", 29.14),
    Item(21, None, 1, "A0", "A2", 27.50),
    Item(20, None, None, None, None, 25.96),
    Item(19, None, None, None, None, 24.50),
    Item(18, None, None, None, None, 23.12),
    Item(17, None, None, None, None, 21.83),
    Item(16, None, None, None, None, 20.60),
    Item(15, None, None, None, None, 19.45),
    Item(14, None, None, None, None, 18.35),
    Item(13, None, None, None, None, 17.32),
    Item(12, None, None, None, None, 16.35),
    Item(11, None, None, None, None, 15.43),
    Item(10, None, None, None, None, 14.57),
    Item(9, None, None, None, None, 13.75),
    Item(8, None, None, None, None, 12.98),
    Item(7, None, None, None, None, 12.25),
    Item(6, None, None, None, None, 11.56),
    Item(5, None, None, None, None, 10.91),
    Item(4, None, None, None, None, 10.30),
    Item(3, None, None, None, None, 9.72),
    Item(2, None, None, None, None, 9.18),
    Item(1, None, None, None, None, 8.66),
    Item(0, None, None, None, None, 8.18),
]