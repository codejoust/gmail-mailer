import lobapi

import makepdf

msg = """
Ms. Sentra Nessen
Dayton Sumner Memorial Art Museum
203 Harbor Street
Baltimore, MD 30040

Dear Ms. Nessen:

I want to thank you for taking the time to interview me yesterday for the
position of assistant director of the Dayton Sumner Memorial Art Museum.
You, Mr. Dawson, and Dr. Acquino exuded warmth, and I know we could all
have an excellent working relationship.

As I further studied the job description for the position, I grew even more
confident that I could take the museum to new heights of success. With the
resources I've gathered, I am ready to hit the ground running with
grant-writing. The 15 percent bonus for grants brought in is an excellent
incentive, and I would devote a significant portion of my time to
this important venture. I also have a number of great ideas for community
and media relations and am excited by your interest in bringing more
schoolchildren to the museum.


As I mentioned when we met, I would like to use my fine arts degree and
journalism minor to enhance the museum's
identity while at the same time meeting the needs and expectations of the
community. I believe I can make a
significant contribution to the fundraising effort, and I am particularly
interested in exploring a corporate donor
program.

I am convinced I could bring a new degree of organization to the museum,
including sinking my teeth into making the
workspace far less chaotic and far more functional. More importantly, I'd
like to get communications on track so that
newsletters and invitations are sent out on a timely basis. I have some
ideas for making the newsletter more userfriendly.
I feel it is extremely important to maintain close communication between
the board and director, and I am
committed to doing so.
Ms. Nessen, I thank you again for considering me for this position. I look
forward to the possibility of working with you.

Sincerely,
John Oakley A Thank
"""

lobapi.deal_with_email_data('hi from auntie!', 'Iain Nash <iain@iain.in>', msg)

#makepdf.createPdf('hi', 'iain nash', 'test', 'buar\nasdfasdf\nasdfasdfasdf\n\nsdfasdf\n\nasdfasd')

