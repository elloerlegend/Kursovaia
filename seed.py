from app import db, Exhibit, Hall, app

with app.app_context():
    # Создаем залы
    hall1 = Hall(name="Хищники", description="Хищники всех континентов")
    hall2 = Hall(name="Мегапауки и слоны", description="Мегапауки, слоны и их окружение")
    hall3 = Hall(name="Арктика", description="Животные, обитающие в арктических условиях")
    hall4 = Hall(name="Пернатые", description="Птицы, обитающие по всему миру")
    hall5 = Hall(name="Бамбуковые леса", description="Животные, обитающие в бамбуковых лесах")
    hall6 = Hall(name="Тропики", description="Тропические леса и их обитатели")
    hall7 = Hall(name="Рептилии", description="Самые древние животные планеты")
    hall8 = Hall(name="Пресноводные и наземные рептилии", description="Рептилии, обитающие в пресной воде и на земле")
    hall9 = Hall(name="Морская жизнь", description="Морские животные, их среда обитания")
    hall10 = Hall(name="Горы", description="Животные, обитающие в высокогорьях")

    # Создаем экспонаты
    exhibit1 = Exhibit(name="Тигр бенгальский", description="Один из крупнейших видов тигров, обитающий в Южной Азии.",
                       species="Млекопитающее", hall=hall1)
    exhibit2 = Exhibit(name="Африканский слон", description="Самое крупное наземное животное, обитающее в Африке.",
                       species="Млекопитающее", hall=hall2)
    exhibit3 = Exhibit(name="Белый медведь",
                       description="Хищник, обитающий в северных регионах и хорошо приспособленный к жизни в холодном климате.",
                       species="Млекопитающее", hall=hall3)
    exhibit4 = Exhibit(name="Японский журавль",
                       description="Большая птица, символизирующая долгую жизнь и счастье в Японии.", species="Птица",
                       hall=hall4)
    exhibit5 = Exhibit(name="Гигантская панда",
                       description="Млекопитающее, известное своим черно-белым окрасом и привычкой есть бамбук.",
                       species="Млекопитающее", hall=hall5)
    exhibit6 = Exhibit(name="Лягушка-древолаз",
                       description="Яркая амфибия с ядовитой кожей, обитающая в тропических лесах.", species="Амфибия",
                       hall=hall6)
    exhibit7 = Exhibit(name="Крокодил нильский", description="Один из самых крупных и опасных хищников среди рептилий.",
                       species="Рептилия", hall=hall7)
    exhibit8 = Exhibit(name="Мадагаскарский черепах",
                       description="Одно из самых крупных видов черепах, обитающее на Мадагаскаре.", species="Рептилия",
                       hall=hall8)
    exhibit9 = Exhibit(name="Дельфин-белуха",
                       description="Морское млекопитающее, известное своей дружелюбной натурой и отличными навигационными способностями.",
                       species="Млекопитающее", hall=hall9)
    exhibit10 = Exhibit(name="Снежный барс",
                        description="Редкий вид крупных кошек, обитающих в горных районах Центральной Азии.",
                        species="Млекопитающее", hall=hall10)
    exhibit11 = Exhibit(name="Леопард", description="Скоростной хищник, обитающий в Африке и Азии.",
                        species="Млекопитающее", hall=hall1)
    exhibit12 = Exhibit(name="Гиена пятнистая",
                        description="Хищник, известный своим жестоким поведением и сильными челюстями.",
                        species="Млекопитающее", hall=hall1)
    exhibit14 = Exhibit(name="Гиена пятнистая",
                        description="Хищник, известный своим жестоким поведением и сильными челюстями, обитающий в саваннах Африки.",
                        species="Млекопитающее", hall=hall1)
    exhibit15 = Exhibit(name="Меховой барс",
                        description="Малый, но опасный хищник, встречающийся в горных районах Центральной и Южной Азии.",
                        species="Млекопитающее", hall=hall1)
    exhibit16 = Exhibit(name="Мегапаук",
                        description="Гигантский паук, существовавший в эпоху динозавров, известен своими размерами и уникальными охотничьими техниками.",
                        species="Членистоногое", hall=hall2)
    exhibit17 = Exhibit(name="Трицератопс",
                        description="Древний травоядный динозавр с тремя рогами, который жил в позднем меловом периоде.",
                        species="Рептилия", hall=hall2)

    exhibit18 = Exhibit(name="Нарвал",
                        description="Морское млекопитающее, известное своим длинным спиральным зубом, напоминающим рог единорога.",
                        species="Млекопитающее", hall=hall3)
    exhibit19 = Exhibit(name="Полярный медведь",
                        description="Один из самых крупных видов медведей, адаптированных к жизни в Арктике.",
                        species="Млекопитающее", hall=hall3)

    exhibit20 = Exhibit(name="Альбатрос",
                        description="Морская птица, известная своими огромными крыльями, которые могут достигать размаха до 3,5 метров.",
                        species="Птица", hall=hall4)
    exhibit21 = Exhibit(name="Папао",
                        description="Тропическая птица, обитающая в Южной Америке, известна своими яркими цветами и отличным вокалом.",
                        species="Птица", hall=hall4)

    exhibit22 = Exhibit(name="Желтый панголин",
                        description="Ночью активный ночной обитатель, защищающийся жесткими чешуйками от хищников.",
                        species="Млекопитающее", hall=hall5)
    exhibit23 = Exhibit(name="Красный панда",
                        description="Малое млекопитающее, обитающее в горах Гималаев и Южном Китае, известное своей любознательностью и ярким окрасом.",
                        species="Млекопитающее", hall=hall5)

    exhibit24 = Exhibit(name="Амазонский попугай",
                        description="Ярко окрашенная птица, обитающая в тропических лесах Амазонки, известна своей умелостью имитировать человеческую речь.",
                        species="Птица", hall=hall6)
    exhibit25 = Exhibit(name="Ягуар",
                        description="Большой хищник, живущий в тропических лесах Центральной и Южной Америки, является одним из самых сильных кошачьих.",
                        species="Млекопитающее", hall=hall6)

    exhibit26 = Exhibit(name="Анкела",
                        description="Маленький, но опасный вид змеи, обитающий в лесах и саваннах Южной Америки.",
                        species="Рептилия", hall=hall7)
    exhibit27 = Exhibit(name="Каменноугольный крокодил",
                        description="Доисторическое существо, обитающее в пресных водах, отличающееся большими размерами и мощными челюстями.",
                        species="Рептилия", hall=hall7)

    exhibit28 = Exhibit(name="Галапагосская черепаха",
                        description="Один из самых долгоживущих видов черепах, обитающий в пресных водах Галапагосских островов.",
                        species="Рептилия", hall=hall8)
    exhibit29 = Exhibit(name="Грязевой хамелеон",
                        description="Небольшая рептилия, обладающая способностью менять цвет в зависимости от окружающей среды.",
                        species="Рептилия", hall=hall8)

    exhibit30 = Exhibit(name="Синий кит",
                        description="Самое крупное животное на планете, обитающее в океанах и питающееся крилем.",
                        species="Млекопитающее", hall=hall9)
    exhibit31 = Exhibit(name="Морской дракон",
                        description="Древнее морское существо, обладающее уникальными защитными механизмами, позволяющими сливаться с окружающей средой.",
                        species="Рыба", hall=hall9)
    exhibit32 = Exhibit(name="Гималайский медведь",
                        description="Редкий вид медведей, обитающий в высокогорьях Гималаев, имеет характерную черную шерсть с белым пятном на груди.",
                        species="Млекопитающее", hall=hall10)
    exhibit33 = Exhibit(name="Тур",
                        description="Предок домашних быков, когда-то обитавший в высокогорьях Европы и Азии.",
                        species="Млекопитающее", hall=hall10)
    db.session.add_all([hall1, hall2, hall3, hall4, hall5, hall6, hall7, hall8, hall9, hall10])
    db.session.add_all([exhibit1, exhibit2, exhibit3, exhibit4, exhibit5, exhibit6, exhibit7, exhibit8, exhibit9, exhibit10, exhibit11, exhibit12, exhibit14, exhibit15, exhibit16, exhibit18, exhibit19, exhibit20, exhibit21, exhibit22, exhibit23, exhibit24, exhibit25, exhibit26, exhibit27, exhibit28, exhibit29, exhibit30, exhibit31, exhibit32, exhibit33])
    db.session.commit()

    print("Данные добавлены!")