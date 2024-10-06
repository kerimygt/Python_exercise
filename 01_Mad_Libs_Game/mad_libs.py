# Get word funtion
def get_word(word_type):
    user_input = input(f"Enter a {word_type} : ")
    return user_input


# noun(isim) - verb(fiil) - adjective(sıfat)

noun_word = get_word("noun")
verb_word = get_word("verb")
adjective_word = get_word("adjective")

story = f""" Gizemli Enigma

Bir zamanlar, II. Dünya Savaşı'nın ortasında, dünyanın dört bir yanında savaşın gölgesi vardı. Müttefikler, düşmanlarının gizli mesajlarını çözmek için ellerinden geleni yapıyorlardı. İşte tam da bu sırada, Almanların geliştirdiği bir şifreleme makinesi, Enigma, tüm dünyayı şaşkına çevirdi.

Bir gece, İngiliz istihbaratının en {adjective_word} kod çözücüsü, {noun_word}, karanlık bir odada Enigma'nın karşısına geçti. Odanın içi {adjective_word} çalışan makinenin tıklamalarıyla doldu. {noun_word}, dikkatlice her harfi dinledi ve not aldı. Enigma, her seferinde yeni bir şifreleme anahtarıyla çalıştığı için çözümlemek imkansızdı.

Ancak {noun_word}, umutsuzluğa kapılmadan önce, tüm zekasını ve bilgisini seferber etti. Geceleri, odasının içinde karanlıkta mum ışığında, şifrelerin ardındaki gizemi çözmeye çalışıyordu.

Bir gün, uzun bir sürenin ardından, {noun_word}, Enigma'nın bir kısmını çözmeyi başardı. İlk başta, tereddütlerle bilgisini test etti ve doğru çözdüğünden emin oldu. Ardından, heyecanla ekibine haber verdi.

{noun_word} ve ekibi, Enigma'nın gizemini çözerek düşmanın sırlarını çözmeye başladılar. Bu, savaşın seyrini değiştiren bir dönüm noktasıydı. Müttefikler, Almanların planlarını önceden {verb_word}, stratejilerini oluşturuyor ve zafer için daha fazla adım atıyorlardı.

Enigma, gizemini yitirmişti, artık sadece bir makineydi. {noun_word} ve ekibi, cesaretleri, zekaları ve azimleriyle tarihin akışını değiştirmişlerdi. Onların hikayesi, sadece bir şifre kırıcı değil, aynı zamanda bir kahramandı.

"""
print(story)
