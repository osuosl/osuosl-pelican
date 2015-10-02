Protein Geometry - What the Heck is That?
=========================================
:date: 2014-03-29
:author: Jack Twilley
:slug: protein-geometry-what-heck
:img: jack-twilley-post.png

When I bumped into my biochemistry professor, Dr. Kevin Ahern, on campus a few
months ago, I had the pleasure of explaining how I actually get to use what I
learned in his class. And at the Open Source Lab of all places. At the lab, I’ve
had the opportunity to work on an open source project called the Protein
Geometry Database (PGD), and my coursework as a food science major with
fermentation science option -- specifically, that course in biochemistry -- has
proven unexpectedly helpful when working on the PGD.

The Protein Geometry Database was originally created in 2008 by Dr. Donald
Berkholz and Dr. P. Andrew Karplus, in conjunction with Peter Krenesky and John
Davidson at the Open Source Lab. An extremely brief summary of the database:
proteins consist of polypeptide chains, which themselves consist of amino acid
residues. The dihedral angles between the residues and other characteristics of
the bonds found within are influenced by the side chains of those residues and
of their neighbors near and far. These characteristics are among the many
attributes that are of interest to researchers like Drs. Berkholz and Karplus,
both of Oregon State University's Department of Biochemistry and Biophysics.
Since that time, the PGD has evolved and matured to fit the needs of researchers
both on- and off-campus, maintained primarily by student developers at the Open
Source Lab. An example of this is the usage of PGD by cancer researchers at Fox
Chase Cancer Center in Philadelphia to improve their understanding of structural
details at the 0.1 angstrom level, which may assist them in identifying
compounds of interest for cancer-fighting drugs.

All software development projects require two sets of skills: those pertaining
to the various technologies (languages, frameworks and the like), and having a
basic understanding of the concepts being modeled. The PGD is written in Python,
and currently uses the Django framework to provide a web interface to a database
containing protein sequences. Having experience with Django and Python is
necessary, but not sufficient, because familiarity with protein structures is
required to truly grok the PGD codebase.

One example from the PGD is Ramachandran plots. These plots help researchers
identify secondary structures in proteins. Two of these structures -- alpha
helices and beta strands -- were discovered by Linus Pauling OSU ‘22. Having
covered these plots and their purpose in biochemistry class gave me a leg up on
understanding the software used to generate the plots in the PGD.

*Hold on tight, we're about to get seriously technical.*

The sequence of amino acid residues in polypeptide chains is the primary
structure, while the interactions between nearby residues generates the
secondary structure. Amino acids are the building blocks of proteins. They are
composed of three groups surrounding a central carbon atom: an amine (-NH2)
group, a carboxylic acid (-COOH) group, and a side chain. A peptide bond is
formed between two amino acids when the amine group from one amino acid loses a
hydrogen atom while the carboxylic group from another amino acid loses a
hydroxide ion. The amino acid residues remain bonded while the hydrogen atom and
hydroxide ion form a water molecule and are lost. The backbone of the
polypeptide chain therefore consists of three atoms per residue: the nitrogen
atom from the amine group, the central carbon atom, and the carbon atom from the
carboxylic acid group. Bonds between these atoms have three dihedral angles
associated with them: phi, psi, and omega. Phi and psi are heavily influenced by
the side chains of the residues while omega is primarily influenced by the
planarity of the peptide bond. For more information on the topic, download
"Biochemistry Free & Easy" by Dr. Kevin Ahern and Dr. Indira Rajagopal at
http://biochem.science.oregonstate.edu/biochemistry-free-and-easy. This was the
textbook for my biochemistry class and is chock-full of Dr. Ahern's poetry and
songs as well as the sort of information one has come to expect from
high-quality college textbooks.
