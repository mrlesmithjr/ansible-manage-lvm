commit 881d5d77fa435ccaa026c3341d0d2ac1fb537b98
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Mon Apr 27 11:26:18 2020 -0400

    Fixing syntax issue for wantlist

commit 89360e3ffef9ff1dbbb5ad525a7ee1d77e6b8895
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Mon Apr 27 11:16:02 2020 -0400

    Trying to fix the subelements lookup for a single element

    This addresses #42. Will need to do some validation testing, etc.

commit c6a7034e4b0b381c5c5b44a15ce7baad7eab9c1b
Author: Charlie Mordant <cmordant1@gmail.com>
Date: Fri Apr 24 17:22:07 2020 +0200

    remove unused molecule env property

commit 883055c33f2d6b4c0df8e61ce49771c451905334
Author: Charlie Mordant <cmordant1@gmail.com>
Date: Thu Apr 23 19:38:35 2020 +0200

    lint

commit 325c2d6240022fe17abf40dffee842ccf79543f1
Author: Charlie Mordant <cmordant1@gmail.com>
Date: Thu Apr 23 19:25:09 2020 +0200

    install xfs

commit 4a1177e420fd9632f77d07ce0a19f89a1515f8eb
Author: Charlie Mordant <cmordant1@gmail.com>
Date: Tue Apr 21 19:01:29 2020 +0200

    use xfs_info on mountpoint instead of lvm

commit 7fd5a8eec9f4b5110929862056ab88c4db3f14de
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Sun Apr 19 01:59:29 2020 -0400

    Only doing a Molecule lint at this time

commit 7e2a076b0a8155015fd21502db860fa89a2114b3
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Sun Apr 19 01:44:38 2020 -0400

    Added Python requirements for testing, etc.

    Closes #33

commit dadb9f24f7ebc2752e6495c4c3569bdee5e0cc68
Author: Charlie Mordant <cmordant1@gmail.com>
Date: Fri Apr 17 13:12:06 2020 +0200

    remove unwanted files

commit 2f63eab727cf7b0b389d0d0cc1a1c7236b71f839
Author: Charlie Mordant <cmordant1@gmail.com>
Date: Fri Apr 17 12:56:31 2020 +0200

    code smells

commit 050f8a56f10d81f7827be53b8c769b1aa5021c00
Author: Charlie Mordant <cmordant1@gmail.com>
Date: Wed Apr 15 19:08:34 2020 +0200

    typo in check

commit b955a6f073b91773f5f90da878268e74872a99e9
Author: Charlie Mordant <cmordant1@gmail.com>
Date: Wed Apr 15 18:54:17 2020 +0200

    remove unwanted newline

commit f81937e9d82bc48f2ee03f6ff462c32bca3da8f0
Author: Charlie Mordant <cmordant1@gmail.com>
Date: Wed Apr 15 18:52:52 2020 +0200

    makes xfs mountpoint repeatable

commit 1c3818e5d06887c01dc0a4b88a39c0561a446300
Author: Charlie Mordant <cmordant1@gmail.com>
Date: Wed Apr 15 17:34:53 2020 +0200

    mistake on remove volume

commit 47f8dae16a096050dccbb8d161f4a18946a6ae73
Author: Charlie Mordant <cmordant1@gmail.com>
Date: Wed Apr 15 17:13:38 2020 +0200

    github action lint

commit 96fa78d6d099d0a48642d377d3e7f30a0c554bdf
Author: Charlie Mordant <cmordant1@gmail.com>
Date: Wed Apr 15 17:07:33 2020 +0200

    remove deprecated machines

commit 17e8ec1058c5cb66b21b15a8d3912ac9980508a9
Author: Charlie Mordant <cmordant1@gmail.com>
Date: Wed Apr 15 16:56:18 2020 +0200

    configured molecule and fix xfs on centos

commit ba5d929fce982af9baa44cfe8ad0b3079133f444
Author: Charlie Mordant <cmordant1@gmail.com>
Date: Wed Apr 15 15:14:30 2020 +0200

    use dots instead of carets

commit ea9109220bb268b5f14e75e38d9fb32c2d79bae5
Author: Charlie Mordant <cmordant1@gmail.com>
Date: Wed Apr 15 14:33:41 2020 +0200

    molecule test and idempotence

commit d8b3a4e93257dfeb79bc8d4ef349acb53f0019dc
Author: Samuel Mutel <smu-dw@deveryware.net>
Date: Mon Oct 14 12:21:03 2019 +0200

    bug: Resize XFS parts is not working

commit b15ecea51d0045a89aae24e4b0c108b35f060b2c
Author: Tony Peña <emperor.cu@gmail.com>
Date: Wed Jun 26 14:56:13 2019 +0200

    Update debian.yml

    Since ansible 2.8.0 must be change way using dict

commit 9788ee5df68798ad94f11c8133b1d62ff409d0e8
Author: Michele Caputo <mikap83@gmail.com>
Date: Mon Apr 8 14:16:04 2019 +0200

    issue #23: extra parenthesis

commit 0f428a0e40d71aea410fbc1aa329203c0b4f15cd
Author: faisalnizam <faisal@logiik.com>
Date: Tue Mar 26 10:48:45 2019 +0400

    FIX LINT FOR BUILD

    FIX LINT FOR BUILD

commit 8957630c04b8befa99c08ed667e43d95198202ce
Author: faisalnizam <faisal@logiik.com>
Date: Tue Mar 26 10:40:11 2019 +0400

    Adding SWAP FileSystem Exception

    Adding Check for SWAP Filesystem if defined skip
    1. SKIP New Filesystem Creation
    2. SKIP mountpoint check

commit 183087e767cbce08ce2da1a3b04f47d3fc03a7e6
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Tue Apr 2 08:03:42 2019 -0400

    Resolves #21

commit b3ef85d4f738597260d9db0d90e84d0f8721259a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Wed Dec 5 08:39:10 2018 -0500

    Added skip codes for ansible-lint

commit 9f4afa7afb3fedc270c44ff1fa357da4b87845c0
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Wed Dec 5 08:00:13 2018 -0500

    Fixing Travis testing and yamllint issues

commit 5603c5f6b0899a1b2cdeeeb3c035eb6249e96fa7
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Wed Dec 5 07:51:31 2018 -0500

    Added Travis testing and hooks for galaxy

commit 563aa1effba936340cbaad9766a49f570292edee
Author: Mark Goddard <mark@stackhpc.com>
Date: Wed Oct 31 11:42:20 2018 +0000

    Fix indentation

commit 4a58cb36cf6d4dd4bb23e86972658be508cca082
Author: Mark Goddard <mark@stackhpc.com>
Date: Wed Oct 31 11:16:27 2018 +0000

    Update tasks/manage_lvm.yml

    Co-Authored-By: oneswig <stig.github@telfer.org>

commit a0c784797f538fc5393d75589ac48e86c51e88db
Author: Stig Telfer <stig@stackhpc.com>
Date: Wed Oct 31 10:16:44 2018 +0100

    Support not formatting volumes.

    Logic to make the filesystem attribute optional, in situations where
    we do not want the volumes formatted.

commit 66368de1d3d2b6712cbf66fc3dd0962705bf86f9
Author: David Castellanos <dcastellanos@fintonic.com>
Date: Mon Dec 18 00:33:45 2017 +0100

    Add opts and mopts support

commit 386cc28bdb58886ed492d3438c9cb088d36de161
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Sun Jun 11 14:57:53 2017 -0400

    Addresses issue #10

    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 0d255cb5ce9e6016a503203c2ed39a70fb0ccd9c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Fri May 5 09:12:25 2017 -0400

    Fixes issue #8

    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit f2d06d0d46086da0191b4dbde0d420e709e3ea01
Author: Stefan Heimberg <kontakt@stefanheimberg.ch>
Date: Thu Apr 6 00:25:55 2017 +0200

    added support for btrfs

commit 7749d0c62a6e1539aff94c57fd2c0eeaf43dd1a0
Author: Kevin Loveland <kevin.loveland@gmail.com>
Date: Fri Nov 18 10:26:16 2016 -0800

    Fixed issue with idempotency of lvol module. See ansible-module-extras issue #428

commit 3ad965237280d534f0aab0027f9ef61701354e8b
Author: Kevin Loveland <kevin.loveland@gmail.com>
Date: Thu Nov 17 15:17:26 2016 -0800

    Changes to adjust to removal of bare vars in Ansible 2.2

commit a82877c290cfe0b62eda90d8874b8e2b62402946
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Sun Oct 2 09:58:47 2016 -0400

    First commit of CHANGELOG

    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 99366fa547faccb0359dd8d3b19cec802640eb95
Author: Rohit Kothari <rohietkothari@gmail.com>
Date: Thu Sep 29 17:59:19 2016 -0700

    Replace system-storage-manager with lvm2 in centos

commit ca1535d774b4e3310fc993841f1f99400612c7a5
Author: Olivier LOCARD <olivier.locard@deveryware.com>
Date: Fri Sep 23 16:21:07 2016 +0200

    Add xfs_growfs for xfs systemfile type.

commit bb87fa8dbff5df50ed376db74a6d2b95f64fd745
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Tue Nov 3 10:39:58 2015 -0500

    updated vars and conditionals

commit 49b20e2e4a80581f1c53559ff4073b3384eae28c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Tue Nov 3 10:24:54 2015 -0500

    updated when conditions

commit 0232734bed92e976376d4c9f2550b515f72f3d54
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Tue Nov 3 10:22:09 2015 -0500

    updated tasks to only work when lvnames is defined

commit 9f592112095208843da1fd69a658bd49c163a7bb
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Tue Nov 3 09:37:38 2015 -0500

    updated vars and meta

commit 686455514d8bc0da70b3440dbc5afe669188d333
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Tue Nov 3 09:22:00 2015 -0500

    cleaned up and fixed all tasks including swap

commit 9f5c61e25599a130e1625e879438561cc1f6a437
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Mon Nov 2 23:38:38 2015 -0500

    added new task

commit a5103ff6396138f531cf8457f16706b6fc90d1d1
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Mon Nov 2 23:38:23 2015 -0500

    changing role tasks and vars

commit c776e9f339f0bcfe987aa571d29411ac44a29526
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Mon Nov 2 21:50:07 2015 -0500

    updated meta

commit 46e0fd1fc2477693fc66aa4b38ac7bde19087047
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Mon Nov 2 21:23:59 2015 -0500

    updated meta

commit d1d99b2f17d3bc46a479af5d01a976686429b7ce
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date: Mon Nov 2 21:23:03 2015 -0500

    first commit
