from emailNextIn import send 
from emailNextIn import logOut


rec_email = "vedprakashgupta463@gmail.com"
file_name = "GGP_Amethi.xlsx"
sub = "We are Ready! U are now Connected to NextIn"
content = '''
            i am VED PRAKASH GUPTA. Founder and CEO of NEXTIN.
            Next Innovation
            #future of technology
            kindly Welcome u for the occasion of software seremani launching from NEXTIN
         '''
html = '<h2 style="color:orange; font-size:15px;">hloo i m Ved</h2>'


send(rec_email , sub , content , file_name , html)
logOut()
