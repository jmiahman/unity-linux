Hello All,
After many attempts in the last few months and even some non attempts, I have decided to use what I would consider
a bootstrap distribution to start development on the new Unity-Linux. After researching a few distributions that
basically adhere to a similar mindset and direction that I would like Unity to follow, and it has been expressed others
would as well, I have chosen to start work on porting rpm to Alpine Linux. Don't get me wrong Alpine already has a
great package managing tool called apk, that in some ways I feel is superior to RPM, however, I am an Linux Systems
Administrator and a majority of my work is done on RHEL systems. There is also no musl based rpm distributions that
I know of at this time. So it presents a challenge and may even somewhat of a niche. We will see. This folder will
have spec files, directions and maybe even scripts, to bring rpm and then package multiple base packages to eventually
create a new leaner meaner Unity Linux. Many of these will initially be based off of Alpine Linux packages, basically
building Alpine through RPM, they will eventually mature however and be modified to better suite Unity Linux.
