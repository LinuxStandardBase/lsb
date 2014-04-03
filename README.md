LSB
===

Linux Standard Base Documentation and Tests

The Linux Standard Base working group is a working group presently under the 
umbrella of the Linux Foundation.

For many years the working group has spent its time focusing on the
production of the LSB specification which consists of a formal written
specification, similar to IEEE or ISO standards, and an accompanying test
suite.

The specification was historically defined as a 'trailing' specification 
to document an
accepted cross section of packages, libraries, and interfaces in Linux
distributions. As the Linux distribution development process has matured, 
in recent years this become a primary focus on the Enterprise distributions,
as so called bleeding development happens in distributions less interested 
in long term stability, and more interested in living at HEAD and in 
continual development. 

As the commercial 
"Linux market" has matured the specification and tests have contributed to
maintaining a certain compatibility across Linux distributions making it
reasonably straight forward for ISVs to treat many distributions as one
Linux platform. At the same time 
with the market acceptance and adoption of Open Source software, 
and the Agile rapid development models, and Test Driven Design, 
a demand has appeared for new interfaces.  The speed
at which these interfaces have been adopted by Linux distributions has
significantly increased such that the creation of a formal specification
and accompanying certification is no longer as important a primary goal. 

Therefore,
at the face to face meeting held during the Linux Foundation Collaboration
Summit in March, 2014, the working group has concluded that rather than
producing a voluminous specification, the working group should transform its
work to emphasize its other role as a neutral venue to discuss and resolve cross-distribution topics
that are important to ISVs and distributors. This new focus will allow the
working group to continue to provide the value of contributing to distribution
compatibility while at the same time being more involved in cross-distribution
discussions.

The LSB 5.0 specification released in 2014 may well be the last of 
its kind. The
specification and tests are in maintenance mode. Bugs will be accepted and
fixed and these bug fixes may be released as updates, i.e. 5.0.1 and others
as needed. However, we do not presently plan to work to produce a new 
LSB 5.1 or 6.0
specification. The specification and accompanying tests remain in the Bazaar
tree ( http://bzr.linuxfoundation.org/loggerhead/lsb/ ) maintained by the
working group. No new development, i.e. large scale addition of new 
interfaces, libraries,
etc., is expected in the Bazaar repository.  That repository will be quiesced 
as to new commits, and parts may be replicated over into a 'git' backing store.

The focus on providing distribution compatibility, where it matters to
distributions, ISVs, and other stakeholders will remain a key goal of the
working group. The approach to the compatibility challenge is that a specific
challenge will be described in a reasonably short document along with a
solution. Once a solution is accepted by a number of distributions it becomes
a de facto standard. Where ever possible one or more tests are to be
implemented that allow distributions to test their compliance to the agreed
upon specification.

The general work flow is that a problem is identified and the problem
statement is formulated. The working copy of the Problem Statement is tracked
in documents/problems. Once a solution statement has been formulated the
document migrates from documents/problems to documents/proposals. The proposal
should be vetted on distribution mailing lists, and as it develops, by a 
matching statement in the version control system, to the precise language 
of the Problem Statement. Major threads in the discussion should be
referenced by pointers included by reference link to the archive 
in the proposal. After a consensus
is reached and implementation can commence, and the proposal becomes a de facto
standard and migrates to documents/specifications. Unless specifically stated
no document should become an accepted specification without an accompanying
test that allows distributions to self monitor their compliance to the
agreed upon de facto standard. An accepted specification contains a list
of distributions that have undertaken to meet the specification and 
have integrated the appropriate test in their distribution test suite.

Contribution guidelines are provided in the Contributing.txt file in the
top level of the repository.
