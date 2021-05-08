import mail
import mail_creator

templatefile = open('mail-templates/reg.html', 'r')
template = mail_creator.TemplateLetter(templatefile.read())
templatefile.close()

template.render(username='Ghaechka', regcomplete_link='https://maxmine2.pythonanywhere.com/login/reg-complete/hiufg3o8uO6tfo83nto87T9863ty98TBOSIUYOtybegoYtobe8btIYTeiuyfeyu')

f = open('ltt.html', 'a')
f.write(str(template))

letter = mail.Letter(str(template), 'Complete registration process')
for _ in range(3):
    letter.send('sofie.litvin@gmail.com')