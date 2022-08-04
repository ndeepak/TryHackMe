Active Directory?
* Directory service developed by Microsoft to manage Windows Domain Networks
* Stores Information related to objects, such as Computers, Users, Printers, etc.
    Like a phone book for Windows
* Authenticates using kerberos tickets.
* Non-windows devices such as Linux machines, firewalls, etc. can also 
 Authenticate to AD via RADIUS or LDAP ()

 Why AD
 * AD is the most commonly used identity management service in the world.
 98% of Fortune 1000 companies implement the service in their Networks
 * Can be exploited without ever attacking patchable exploits.
 * Instead, we abuse features, trusts, components, and more. (POLICIES)


Physical AD components
    Domain Controllers
    A domain Controller is a server with AD DS server role installed that has 
    specifically been promoted to a domain controller.

Domain Controllers:
* Host a copy of the AD DS(Active Directory Data Store) Directory store.
* Provide Authentication and authorization services.
* Replicate updates to other domain controllers in the domain and forest.
* Allow administrative access to manager user accounts and network resources.


AD DS(DataStore)
The AD DS data store contains the database files and processes that store
and manage Directory information for users, services, and applications.
The AD DS data store:
* Contains the NTDS.dit - a database that contains all of the information of an Active Directory domain controller as well as password hashes for domain users
* is stored by default in the %SystemRoot%\NTDS folder on all domain controllers
* is accessible only through the domain controller processes and protocols


Logical AD components
AD DS Schema
* Defines every type of object that can be stored in the Directory
* Enforces rules regarding object creation and configuration

Object Types            Function                    Examples
Class               what objects can be created     * User
                    in the Directory                * Computers
Attribute Object    Information that can be         * Display name
                    attached to an Object

Domains
Domains are used to group and manage objects in an organization
* An administrative boundary for applying policies to groups of objects
* A replication boundary for replicating data between domain controllers
* An Authentication and authorization boundary that provides a way to limit the scope of access to resources.


Trees
* multiple domains make trees.
A domain tree is a hierarchy of domains in AD DS
All domains in the tree:
* Share a contiguous namespce with the parent domain
* Can have additional child domains.
* By default create a two-way transitive trust with other domains.


Forests
A forest is a collection of one or more domain Trees
Forests:
* share a common Schema
* share a common configuration partition
* share a common global catalog to enable searching
* enable trusts between all domains in the forest
* share the enterprise admins and schema admins groups

Organizational Units (OUS)
Ous are AD containers that can contain users, groups, computers, and other ous.
OUs are used to:
* Represent your organization hierarchically and logically.
* Manage a collection of objects in a consistent way
* Delegate permissions to administer groups of objects
* Apply policies


Trusts
Trust provide a mechanism for users to gain access to resources in another domain.

Types of trusts:
Directional: The trust direction flows from trusting domain to the trusted domain

Transitive: The trust relationship is extended beyond a two-domain trust to include other trusted domains.

* All domains in a forest trust all other domains in the forest
* trusts can extend outside the forest.


## Object

User
* Enables network resource access for a user

InetOrgPerson
* Similar to a user account
* Used for compatibility with other directory services

Contacts
* Used primarily to assign e-mail addresses to external users.
* Does not enable network access

Groups
* Used to simplify the administration of access control

Computers
* Enables authentication and auditing of computer access to resources

Printers
* Used to simpliy the process of locating and connecting to printers

Shared folders
* Enables users to search for shared folders based on properties