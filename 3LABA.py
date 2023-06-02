from PIL import Image
from Crypto.Cipher import AES
from Crypto import Random
from datetime import datetime

key_generator = lambda size: Random.new().read(size) 

# Количество байт при шифровании AES-128 должно быть кратное 16, 
# поэтому недостающие необходимо заполнить b"\x00" означает 0x00
checkImage = lambda image_b: image_b + b"\x00" * (16 - len(image_b) % 16)

RGB = lambda data: tuple(zip([data[i] for i in range(0, len(data)) if i % 3 == 0],
                             [data[i] for i in range(0, len(data)) if i % 3 == 1],
                             [data[i] for i in range(0, len(data)) if i % 3 == 2]))

def create_result_image(result, cipher):
    image_ecb = Image.new(image.mode, image.size)
    image_ecb.putdata(result)
    image_ecb.save(f"tux{cipher}.png", "PNG")

cipher = lambda mode, mode_str: create_result_image(RGB(AES.new(key, mode)
                                .encrypt(checkImage(image_bytes))[:len(image_bytes)]), mode_str)

image = Image.open("tux.png")
image_bytes = image.convert("RGB").tobytes()
key = key_generator(16)

# Режим шифрования ECB (Electronic Codebook) – 
# это простейший режим шифрования, при котором вся последовательность 
# данных разбивается на блоки фиксированной длины (16 байт), которые затем независимо 
# шифруются одним и тем же шифром. Каждый блок открытого текста шифруется одним 
# и тем же ключом. Это означает, что если один и тот же блок встретится несколько раз в открытом тексте,
# он будет шифроваться в одинаковые блоки шифротекста. Таким образом, позволяет эффективно шифровать данные,
# но при этом не обеспечивает никакой дополнительной безопасности.
start_time = datetime.now()
cipher(AES.MODE_ECB, "ECB")
print("Шифр ECB выполнен. \nВремя:", datetime.now() - start_time, end = "\n\n")


# Режим шифрования CBC (Cipher Block Chaining) – это режим, который решает проблемы режима ECB,
# связанные с одинаковостью шифротекста. В режиме CBC каждый блок открытого текста XOR'ится с
# предыдущим блоком шифротекста перед шифрованием. Это означает, что каждый блок шифротекста 
# зависит от предыдущего блока. Использование вектора инициализации (IV) гарантирует уникальность
# первого блока шифротекста. Режим CBC обеспечивает более высокий уровень безопасности по сравнению
# с режимом ECB.
start_time = datetime.now()
cipher(AES.MODE_CBC, "CBC")
print("Шифр CBC выполнен. \nВремя:", datetime.now() - start_time, end = "\n\n")

# Режим шифрования CFB (Cipher Feedback) – это режим, который позволяет шифровать открытый
# текст произвольной длины. Режим CFB похож на режим CBC тем, что каждый бит открытого текста XOR'ится
# с предыдущим блоком шифротекста. Однако в режиме CFB не применяется блоковый шифр, к каждому блоку 
# применяется последовательный процесс шифрования. Это означает, что длина блоков открытого текста и 
# шифротекста может быть разной. Режим CFB обеспечивает индивидуальное шифрование каждого бита 
# открытого текста, что делает его более безопасным, чем режим ECB.
start_time = datetime.now()
cipher(AES.MODE_CFB, "CFB")
print("Шифр CFB выполнен. \nВремя:", datetime.now() - start_time, end = "\n\n")

# Режим шифрования OFB (Output Feedback) – это режим, который позволяет использовать 
# симметричные алгоритмы шифрования для создания потоковых шифров. Режим OFB использует в 
# качестве шифратора генератор псевдослучайной последовательности, который обрабатывает 
# блоки начального значения IV с помощью блочного шифра. Затем производится XOR'ирование 
# полученного блока шифротекста с открытым текстом, чтобы получить получить шифротекст. 
# Режим OFB обеспечивает независимость шифрования каждого блока.
start_time = datetime.now()
cipher(AES.MODE_OFB, "OFB")
print("Шифр OFB выполнен. \nВремя:", datetime.now() - start_time, end = "\n\n")







