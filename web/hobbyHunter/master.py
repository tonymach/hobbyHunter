class Master(object):
    """
    This file is updated with whether the production is local or external,
    as well as many other default values
    """
    def __init__(self):
        self.isLocal = False    
        self.isExternalDb = False
        self.trialSessions = 10

        #
        # Asii art, for motivational purposes of course.
        #

        self.loadupAscii = """

 /$$   /$$           /$$       /$$                       /$$   /$$                       /$$
| $$  | $$          | $$      | $$                      | $$  | $$                      | $$
| $$  | $$  /$$$$$$ | $$$$$$$ | $$$$$$$  /$$   /$$      | $$  | $$ /$$   /$$ /$$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$
| $$$$$$$$ /$$__  $$| $$__  $$| $$__  $$| $$  | $$      | $$$$$$$$| $$  | $$| $$__  $$|_  $$_/   /$$__  $$ /$$__  $$
| $$__  $$| $$  \ $$| $$  \ $$| $$  \ $$| $$  | $$      | $$__  $$| $$  | $$| $$  \ $$  | $$    | $$$$$$$$| $$  \__/
| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$      | $$  | $$| $$  | $$| $$  | $$  | $$ /$$| $$_____/| $$
| $$  | $$|  $$$$$$/| $$$$$$$/| $$$$$$$/|  $$$$$$$      | $$  | $$|  $$$$$$/| $$  | $$  |  $$$$/|  $$$$$$$| $$
|__/  |__/ \______/ |_______/ |_______/  \____  $$      |__/  |__/ \______/ |__/  |__/   \___/   \_______/|__/
                                         /$$  | $$
                                        |  $$$$$$/       -- Madness at it's very finest.
                                         \______/
Loaded * * *


       """
        self.workinMessage = """

                        `"-._
                      `. "-._
                        T.   "-.
                         $$p.   "-.
                         $$$$b.    `,
                      .g$$$$$$$b    ;
                    .d$$$$$$$$$$;   ;
                 __d$$$$$$P""^T$$   :
               .d$$$$P^^""___       :
              d$P'__..gg$$$$$$$$$$; ;
             d$$ :$$$$$$$$$$$$$$$$;  ;
            :$$; $$$$$$$$$$$$$$$$P  :$
            $$$  $$$$$$$$$$$$$$$$b  $$
           :$$$ :$$$$$$$$$$$$$$$$$; $$;
           $$$; $$$$$$$$$$$$$$$$$$; $$;
          :$$$  $$$$$$$$$^$$$$$$$$$ :$$
          $$$; :$$$p__gP' `Tp__g$$$ :$$
         :$$$  $$P`T$P' .$. `T$P'T$; $$;
         $$$; :$$;     :P^T;     :$; $$;
        :$$$  $$$$-.           .-$$$ :$$
        $$$$ :$$$$; \   T$P   / :$$$  $$
       :$$$; $$$$$$  ; b:$;d :  $$$$; $$;
       $$$$; $$$$$$; : T T T ; :$$$$$ :$$
    .g$$$$$  :$$$$$$  ;' | ':  $$$$$$  T$b
 .g$$$$$$$$   $$$$$$b :     ; d$$$$$;   `Tb
:$$$$$$$$$;   :$$$$$$$;     :$$$$$$P       \\
:$$$$$$$$$;    T$$$$$$$p._.g$$$$$$P         ;
$$$P^^T$$$$p.   `T$$$$$$$$$$$$$$P'     _/`. :
       `T$$$$$b.  `T$$$$$$$$$$P'    .g$P   \;
  bug    `T$$$$$b.  "^T$$$$P^"     d$P'
           `T$$$$$b.             .dP'
             "^T$$$$b.        .g$P'
                "^T$$$b    .g$P^"
                   "^T$b.g$P^"
                      "^$^"

        You're killin it you motherf*cker.

"""


    def local(self):
        return self.isLocal

    def externalDb(self):
        return self.isExternalDb

    def trialSessionCount(self):
        return self.trialSessions

    def workin(self):
        print(self.workinMessage)
    def loadup(self):
        print(self.loadupAscii)

global master, workin

master = Master()
