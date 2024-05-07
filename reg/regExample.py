import re

class regExample:
    def __init__(self) -> None:
        pass

    @staticmethod
    def buscar(texto:str) -> list:
        #patrón palabras que empiezan en vocal minúscula
        patron = "\\b[aeiou][^\\s., ]*"
        result = re.findall(patron, texto)
        return result
    
    @staticmethod
    def validURL(url:str) -> bool:
        patron = "^https?://.+(\w+[.#=]\w+[.#=]?)"
        result = re.findall(patron, url)
        return result
    
if __name__ == "__main__":
    url = "https://regex101.com"
    text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis finibus, odio sed lacinia posuere, mi ex placerat diam, id vestibulum libero nunc quis massa. Vestibulum quam dui, mollis vitae libero vitae, ornare mollis eros. Donec aliquet semper elit, vel consectetur magna semper a. Vestibulum mauris nisi, venenatis eget sapien ut, auctor faucibus urna. Fusce gravida ac nisi eu venenatis. Sed elementum dolor orci, at ornare ligula finibus ut. Donec ac massa risus. Aliquam imperdiet neque nec dui sollicitudin pharetra. Aenean finibus neque enim, in porttitor nisi finibus eu. Etiam dapibus enim ipsum. Mauris nec semper velit. Donec vitae ullamcorper odio, at posuere ipsum. In ut consequat augue. Curabitur non massa sollicitudin massa mattis luctus. Pellentesque posuere elit eu nunc laoreet accumsan.

Duis tincidunt, arcu et pretium auctor, nunc odio ultricies ante, at suscipit risus lorem in turpis. Aenean ut augue et odio egestas dapibus in eget purus. Etiam volutpat metus dolor, varius vulputate nibh cursus vitae. Aliquam erat volutpat. Mauris dapibus ultricies est, sed fringilla sem placerat id. Donec lacinia nunc eget purus dapibus finibus a eu velit. Ut sit amet est eget ipsum aliquet sagittis id in ex. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec id risus in ligula tristique rutrum eu ac felis. Donec id nunc aliquam sapien hendrerit pulvinar maximus id sem. Praesent in mauris lectus. Integer iaculis sapien est, vitae gravida sapien sodales eu.

Suspendisse est tellus, lobortis non facilisis et, vulputate in felis. Sed sodales aliquet lorem, nec maximus nisl malesuada ut. Mauris finibus elementum fringilla. Nunc dictum vulputate sem vitae dapibus. Nullam non dui urna. Vivamus libero enim, scelerisque at est vel, luctus sagittis diam. Sed scelerisque tellus ac condimentum dapibus. Etiam lacus nibh, tempor a fringilla eget, viverra in sem. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent id tempus risus. Nullam vel nisl sit amet ipsum consequat commodo. Sed rutrum magna in velit lacinia tempus.

Integer iaculis ornare nulla et ultricies. Donec dapibus sem ut dolor aliquam, id imperdiet risus dapibus. Sed facilisis, magna in laoreet tristique, arcu sapien ultricies est, a luctus urna neque nec mi. Aliquam tristique rhoncus turpis in euismod. Quisque sit amet tortor sodales, elementum massa id, auctor risus. Praesent non lorem orci. Pellentesque ante nisi, elementum eget ex vitae, ornare interdum sem. Donec cursus eros vitae quam aliquam ornare.

Pellentesque sem arcu, vulputate non nisl eu, mattis viverra magna. Mauris id scelerisque quam. Duis volutpat metus at rutrum scelerisque. Quisque purus diam, congue convallis augue ac, porta porttitor eros. Vestibulum consequat orci ac purus malesuada, in lacinia leo placerat. Donec pharetra sapien lectus, vitae dapibus enim facilisis nec. Vivamus fermentum, est vitae elementum porttitor, leo felis tempus nisi, quis mollis odio diam vel magna. Morbi a felis lacus. Proin mattis dictum tellus. Vivamus aliquam nibh venenatis eros maximus rutrum. Integer ante nunc, pellentesque ac dolor sit amet, vestibulum maximus sapien. Cras porttitor dolor convallis urna convallis iaculis. Sed vulputate leo sit amet augue faucibus rhoncus. Nunc consectetur, tortor a scelerisque efficitur, lectus metus porttitor leo, vel semper quam justo vel purus. Morbi placerat dapibus orci, sed consequat purus lacinia sed.
'''