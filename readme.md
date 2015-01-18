## Gmail -> Snail Mail

This project takes emails in a certain gmail inbox, will eventually search for google wallet cash to validate the transaction, then send a request to lob by parsing out the address, your address (from an original setup email), and then goes through the body of the message to format it professionally before it mails it then emails you in confirmation.

Enjoy!


### Example Email confirmation:


    Lob Mailer <lobthat@gmail.com>
    To: Iain Nash
    Subject: Sent letter! <lobthat@gmail.com>
    9:10 AM (0 minutes ago)

        Just a confirmation that your letter has been sent at http://assets.lob.com/obj_b51c0cba93291dfc.pdf

        Thanks for using lobthat@gmail.com,
        The lobthat team
        

### Example Readout:

    ➜  HackPENN  python check_emails.py
    Fetching new email :).
    Fetching 2 messages.
    ('+OK message follows', ['Delivered-To: lobthat@gmail.com', 'Subject: thanks sentra', 'From: Iain Nash <allelectricthings@gmail.com>', 'To: lobthat@gmail.com, ', 'Content-Type: multipart/alternative; boundary=e89a8f646b13a3f674050cec85d5', '', '--e89a8f646b13a3f674050cec85d5', 'Content-Type: text/plain; charset=UTF-8', '', 'Ms. Sentra Nessen', 'Dayton Sumner Memorial Art Museum', '203 Harbor Street', 'Baltimore, MD', '', 'Dear Ms. Nessen:', '', 'I want to thank you for taking the time to interview me yesterday for the', 'position of assistant director of the Dayton Sumner Memorial Art Museum.', 'You, Mr. Dawson, and Dr. Acquino exuded warmth, and I know we could all', 'have an excellent working relationship.', '', 'As I further studied the job description for the position, I grew even more', 'confident that I could take the museum to new heights of success. With the', "resources I've gathered, I am ready to hit the ground running with", 'grant-writing. The 15 percent bonus for grants brought in is an excellent', 'incentive, and I would devote a significant portion of my time to', 'this important venture. I also have a number of great ideas for community', 'and media relations and am excited by your interest in bringing more', 'schoolchildren to the museum.', '', '', 'As I mentioned when we met, I would like to use my fine arts degree and', "journalism minor to enhance the museum's", 'identity while at the same time meeting the needs and expectations of the', 'community. I believe I can make a', 'significant contribution to the fundraising effort, and I am particularly', 'interested in exploring a corporate donor', 'program.', '', 'I am convinced I could bring a new degree of organization to the museum,', 'including sinking my teeth into making the', "workspace far less chaotic and far more functional. More importantly, I'd", 'like to get communications on track so that', 'newsletters and invitations are sent out on a timely basis. I have some', 'ideas for making the newsletter more userfriendly.', 'I feel it is extremely important to maintain close communication between', 'the board and director, and I am', 'committed to doing so.', 'Ms. Nessen, I thank you again for considering me for this position. I look', 'forward to the possibility of working with you.', '', 'Sincerely,', 'John Oakley A Thank', '', '--e89a8f646b13a3f674050cec85d5', 'Content-Type: text/html; charset=UTF-8', 'Content-Transfer-Encoding: quoted-printable', '', '<div dir=3D"ltr"><div>Ms. Sentra Nessen</div><div>Dayton Sumner Memorial Ar=', 't Museum</div><div>203 Harbor Street</div><div>Baltimore, MD</div><div><br>=', '</div><div>Dear Ms. Nessen:</div><div><br></div><div>I want to thank you fo=', 'r taking the time to interview me yesterday for the position of assistant d=', 'irector of the Dayton Sumner Memorial Art Museum. You, Mr. Dawson, and Dr. =', 'Acquino exuded warmth, and I know we could all have an excellent working re=', 'lationship.</div><div><br></div><div>As I further studied the job descripti=', 'on for the position, I grew even more confident that I could take the museu=', 'm to new heights of success. With the resources I&#39;ve gathered, I am rea=', 'dy to hit the ground running with grant-writing. The 15 percent bonus for g=', 'rants brought in is an excellent incentive, and I would devote a significan=', 't portion of my time to</div><div>this important venture. I also have a num=', 'ber of great ideas for community and media relations and am excited by your=', ' interest in bringing more schoolchildren to the museum.</div><div><br></di=', 'v><div><br></div><div>As I mentioned when we met, I would like to use my fi=', 'ne arts degree and journalism minor to enhance the museum&#39;s</div><div>i=', 'dentity while at the same time meeting the needs and expectations of the co=', 'mmunity. I believe I can make a</div><div>significant contribution to the f=', 'undraising effort, and I am particularly interested in exploring a corporat=', 'e donor</div><div>program.</div><div><br></div><div>I am convinced I could =', 'bring a new degree of organization to the museum, including sinking my teet=', 'h into making the</div><div>workspace far less chaotic and far more functio=', 'nal. More importantly, I&#39;d like to get communications on track so that<=', '/div><div>newsletters and invitations are sent out on a timely basis. I hav=', 'e some ideas for making the newsletter more userfriendly.</div><div>I feel =', 'it is extremely important to maintain close communication between the board=', ' and director, and I am</div><div>committed to doing so.</div><div>Ms. Ness=', 'en, I thank you again for considering me for this position. I look forward =', 'to the possibility of working with you.</div><div><br></div><div>Sincerely,=', '</div><div>John Oakley A Thank=C2=A0</div>', '</div>', '', '--e89a8f646b13a3f674050cec85d5--'], 6391)
    ----- email ----
    Iain Nash <CENSORED@gmail.com>
    thanks sentra
    Ms. Sentra Nessen
    Dayton Sumner Memorial Art Museum
    203 Harbor Street
    Baltimore, MD

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

    sending content
    Ms. Sentra Nessen
    Dayton Sumner Memorial Art Museum
    203 Harbor Street
    Baltimore, MD
    filename
    tmp.pdf
    filename
    {
      "date_created": "2015-01-18T13:53:21.776Z",
      "date_modified": "2015-01-18T13:53:21.776Z",
      "double_sided": 0,
      "full_bleed": 0,
      "id": "obj_465d77e177c9e6bc",
      "name": "Mainfile",
      "object": "object",
      "pages": 1,
      "quantity": 1,
      "setting": {
        "color": "black and white",
        "description": "black and white document",
        "id": "100",
        "length": "11.000",
        "notes": "12 cents per extra page",
        "object": "setting",
        "paper": "20lb paper standard",
        "type": "documents",
        "width": "8.500"
      },
      "template": 0,
      "thumbnails": [
        {
          "large": "http://assets.lob.com/obj_465d77e177c9e6bc_thumb_large_1.png",
          "medium": "http://assets.lob.com/obj_465d77e177c9e6bc_thumb_medium_1.png",
          "small": "http://assets.lob.com/obj_465d77e177c9e6bc_thumb_small_1.png"
        }
      ],
      "url": "http://assets.lob.com/obj_465d77e177c9e6bc.pdf"
    }
    deleting message
    Done fetching messages
    waiting for new messages...
