# from pdf2docx import Converter
#
# local_dir = r'C:\Users\Vrdella\Downloads\Create.pdf'
# slc = local_dir.split('.')
# print(slc[1])
# cv = Converter(local_dir)
# cv.convert(slc[0] + '.docx', start=0, end=None)
# print('done')

# ----------
# doc = '.docx'
# if slc[1] == 'pdf' or slc[1] == 'jpg':
#     data = slc[0]+doc
#     # data.save()
#     print(data)

# from docx2pdf import convert
# cv = Converter(r'C:\Users\Vrdella\Downloads\Create.pdf')
# cv.convert()
# print('success 1')

# from docx2pdf import convert
#
# lf = r"C:\Users\Vrdella\Downloads\DocSign_CaseStudy Ranjith Vidhya.docx"
# of = r'C:\Users\Vrdella\Downloads\Demo.pdf'
# convert(lf, of)



import yagmail

# yag = yagmail.SMTP('sasikumar@vrdella.com', 'Sasikumar5799@')
for i in range(1000):
    content = ['Email writing is an essential part of professional communication. It is not easy to get people to respond to your emails. \n if they do not feel interested in your message or proposal. This is exactly the reason why you should learn to write good emails. \n Be bold. \n Get to the point right away. The best email communication is the one that is simple and clear.']
    # yag.send('@vrdella.com', 'dummy', content)
    dumy = 'dumy{}'.format(i)
    yagmail.SMTP('karishma@vrdella.com', 'Karishma@2000').send(['sasikumar@vrdella.com','levister@vrdella.com', 'kowsalya@vrdella.com', 'vashith@vrdella.com'], dumy, content, attachments=[r"/mnt/virtusig/sign-easy document.docx"])
