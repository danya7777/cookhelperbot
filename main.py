import telebot
from telebot import types

bot = telebot.TeleBot("6053147770:AAGaoFxKyYHNnl086JN8IzytWXBeDfxs9G4")

@bot.message_handler(commands = ['start'])
def start(message):
	bot.send_message(message.chat.id, '👋')
	bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} {message.from_user.last_name}! \n Чтобы начать использовать меня необходимо написать блюдо рецепт которого ты хочешь узнать.')

@bot.message_handler(commands = ['list'])
def list_of_dishes(message):
	bot.send_message(message.chat.id, '📖')
	bot.send_message(message.chat.id, f'Вот все блода к которым я могу показать вам рецепт: \nВареники\nГречка\nПельмени\nСалат\nАмериканские блины\nЯишница')
		
@bot.message_handler(commands = ['help'])
def help(message):
	bot.send_message(message.chat.id, '❓')
	bot.send_message(message.chat.id, 'Это справка. Если ты читаешь это то тебе наверняка нужна моя помощь или ты обнаружил ошибку или баг.\n\n\n\nЕсли это так, то пиши ко мне на почту mishindaniil365247@gmail.com')
	
@bot.message_handler()
def dishes(message):	
	if message.text == 'вареники' or message.text == 'Вареники':
	# Рецепт вареников
		bot.send_message(message.chat.id, f'Хорошо {message.from_user.first_name}. Для этого нужны эти ингредиенты:\nмука				 3 стакана\nвода - 0.5 стакана\nмолоко - 0.5 стакана\nрастительное масло - 1 чайная ложка\nяйцо - 1 штука\nспеции - по вкусу\nсоль - по вкусу. \n1.Очистите картошку, поставьте варить, посолите.\n2.Пока варится картошка, начинаем замешивать тесто. Для этого нужно высыпать в миску муку. Cмешиваем яйцо, молоко, воду и соль.\n3.Выливаем эту смесь в муку, замешиваем тесто, добавляем масло. Готовое тесто накрываем тряпочкой и оставляем на 40 минут.\n4.Сделать из картофеля пюре, соль и перец по вкусу, можно добавить укроп. Оставляем остывать картошку.\n5.Тесто раскатываем и нарезаем.\n6.Берем картофель и лепим вареники.\n7.Ставим кастрюлю с водой, доводим до кипения.\n8.Когда вода закипает, бросаем в нее слепленные вареники. Подаем с маслом или сметаной.')
		bot.send_message(message.chat.id, '😋') 
	elif message.text == 'гречка' or message.text == 'Гречка' :
	# Рецепт гречки
		bot.send_message(message.chat.id, f'Хорошо {message.from_user.first_name}. Для этого нужны следующие ингредиенты:\nкрупа гречневая (ядрица) – 2 стакана\nсоль – 1/2 ч. л.\nвода – 4 стакана\nмасло растительное – 1,5 ст. л.\n1.Гречку тщательно перебрать, разложив в один слой на столе, затем промыть в нескольких водах. Обсушить в дуршлаге\n2.Раскалить сухую сковороду и обжарить гречку, постоянно помешивая, до золотистого цвета, 4–5 минут. Предварительное обжаривание крупы делает ее более ароматной и рассыпчатой, а также уменьшает время приготовления.\n2.Вскипятить в большой кастрюле слегка подсоленную воду. Пропорция воды и крупы всегда одинакова: на 1 часть гречки 2 части воды. Всыпать обжаренную гречку и довести на сильном огне до кипения.\n4.После закипания снять шумовкой пену, добавить растительное масло. Уменьшить огонь и варить гречку 6–8 минут. Снять с огня, накрыть крышкой и дать настояться еще несколько минут.')
		bot.send_message(message.chat.id, '😋') 
	elif message.text == 'пельмени' or message.text == 'Пельмени':
	# Рецепт пельменей
		bot.send_message(message.chat.id, f'Хорошо {message.from_user.first_name}. Для этого нам нужны следующие ингредиенты:\n1 яйцо\n200 мл воды\n1 ч. л. соли\n600 г пшеничной муки\n250 г говяжьего фарша\n250 г свиного фарша\n1 большая луковица\n1 зубчик чеснока\nсоль и черный перец.\n1.Приготовить тесто для русских пельменей. Муку просеять горкой. Сделать сверху углубление, влить в него яйцо и 1 ст. л. воды, добавить щепотку соли.\n2.Собирая муку с краев к середине, чтобы вода и яйцо не выливались из углубления, замешивать тесто, добавляя небольшими порциями оставшуюся воду. Месить тесто для пельменей до тех пор, пока оно не станет эластичным и однородным, примерно 10 мин. Накрыть влажным полотенцем и оставить на 30 мин. Вода для пельменного теста должна быть ледяная. Для этого ее заранее ставят в холодильник или морозильник.\n3.Пока расстаивается тесто, приготовить начинку для пельменей. Лук и чеснок очистить и очень мелко порубить. Смешать говяжий и свиной фарш, добавить лук с чесноком, посолить, поперчить. Тщательно перемешать до однородности.\n4.Готовое тесто для русских пельменей разделить на 4 части. 3 части накрыть влажным полотенцем и отложить. Оставшееся тесто скатать в жгут толщиной 2 см. Нарезать его на кусочки шириной 1,5 см. На присыпанной мукой поверхности раскатать каждый кусочек теста в тонкую лепешку.\n5.Выложить в центр каждой лепешки по 1,5 ч. л. начинки, сложить кружок с начинкой пополам так, чтобы получился полумесяц. Соединить концы полумесяца и скрепить их. Плотно прижать пальцами, чтобы пельмени не разваливались при варке.\n6.Выложить пельмени на поднос или плоское блюдо, присыпать мукой и поставить в холодильник. Так же приготовить пельмени из оставшегося теста.\n7.Затем надо сварить эти пельмени до готовности на медленном огне. Рекомендуется подавать со сметаной.')
		bot.send_message(message.chat.id, '😋') 
	elif message.text == 'салат' or message.text == 'Салат':
		# Рецепт салата
		bot.send_message(message.chat.id, f'Хорошо {message.from_user.first_name}. Вообще можно экспериментировать с ингредиентами, но самый простой салат состоит из помидоров и огурцов. Для этого моем и нарезаем овощи в миску. Затем солим, перчим, добавляем кефир, сметану или растительное (оливковое и т. д.) масло и перемешиваем.')
		bot.send_message(message.chat.id, '😋')
	elif message.text == 'Американские блины' or message.text == 'американские блины':
		# Рецепт блинов
		bot.send_message(message.chat.id, f'Хорошо {message.from_user.first_name}. Для этого нам нужны следующие ингредиенты:\nКуриное яйцо - 2 штуки\nСоль - 1 чайная ложка\nСахар - 3 столовые ложки\nМолоко - 2 стакана\nПшеничная мука - 2 стакана\nГашеная сода - 1 чайная ложка\nРастительное масло - 1/4 стакана\n\n1.Яйца взбить с сахаром и солью до появления пены.\n2.Добавить стакан молока, хорошо взбить венчиком, постепенно всыпать муку, постоянно разбивая комочки венчиком.\n3.Повторить предыдущий пункт, добавив оставшиеся стаканы молока и муки.\n4.Влить растительное масло (можно заменить топленым сливочным).\n5.Погасить соду, добавить в тесто и еще раз хорошо перемешать. Оставить постоять минут 5–10. За это время разогреть сковороду.6.Жарить на умеренном огне. Как только появятся и начнут лопаться пузырьки, перевернуть оладушек и жарить еще секунд 20.')
		bot.send_message(message.chat.id, '😋')
	elif message.text == 'яишница' or message.text == 'Яишница' or message.text == 'Яичница' or message.text == 'яичница':
		bot.send_message(message.chat.id, 'иорфккр')
	else:
	# Error 404
		bot.send_message(message.chat.id, 'Извините но я вас не понимаю(((\nПопробуйте переписать или перефразировать ваше сообщение. Но если вы все правильно написали, значит я не знаю такого блюда. Ожидайте следующих обновлений или посмотрите на блюда которые я умею готовить с помощью команды /list')
		bot.send_message(message.chat.id, '🫤')
		
bot.polling(none_stop = True)
