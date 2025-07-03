https://owasp.org/www-project-mobile-top-10/2016-risks/

M1: Improper Platform Usage
Threat Agents
Application Specific

This category covers misuse of a platform feature or failure to use platform security controls. It might include Android intents, platform permissions, misuse of TouchID, the Keychain, or some other security control that is part of the mobile operating system.

Attack Vectors
Exploitability EASY

The attack vectors correspond to the same attack vectors available through the traditional OWASP Top Ten. Any exposed API call can serve as attack vector here.

Security Weakness
Prevalence COMMON
Detectability AVERAGE

In order for this vulnerability to be exploited, the organization must expose a web service or API call that is consumed by the mobile app. The exposed service or API call is implemented using insecure coding techniques that produce an OWASP Top Ten vulnerability within the server. Through the mobile interface, an adversary is able to feed malicious inputs or unexpected sequences of events to the vulnerable endpoint. Hence, the adversary realizes the original OWASP Top Ten vulnerability on the server.

Technical Impacts
Impact SEVERE

The technical impact of this vulnerability corresponds to the technical impact of the associated vulnerability (defined in the OWASP Top Ten) that the adversary is exploiting via the mobile device.

For example, an adversary may exploit a Cross-Site Scripting (XSS) vulnerability via the mobile device. This corresponds to the OWASP Top Ten A3 - XSS Category with a technical impact of moderate.

Business Impacts
Application / Business Specific

The business impact of this vulnerability corresponds to the business impact of the associated vulnerability (defined in the OWASP Top Ten) that the adversary is exploiting via the mobile device.

For example, an adversary may exploit a Cross-Site Scripting (XSS) vulnerability via the mobile device. This corresponds to the OWASP Top Ten A3 - XSS Category’s business impacts.

Am I Vulnerable To ‘Improper Platform Usage’?
The defining characteristic of risks in this category is that the platform (iOS, Android, Windows Phone, etc.) provides a feature or a capability that is documented and well understood. The app fails to use that capability or uses it incorrectly. This differs from other mobile top ten risks because the design and implementation is not strictly the app developer’s issue.

There are several ways that mobile apps can experience this risk.

Violation of published guidelines. All platforms have development guidelines for security (c.f., ((Android)), ((iOS)), ((Windows Phone))). If an app contradicts the best practices recommended by the manufacturer, it will be exposed to this risk. For example, there are guidelines on how to use the iOS Keychain or how to secure exported services on Android. Apps that do not follow these guidelines will experience this risk.

Violation of convention or common practice. Not all best practices are codified in manufacturer guidance. In some instances, there are de facto best practices that are common in mobile apps.

Unintentional Misuse. Some apps intend to do the right thing, but actually get some part of the implementation wrong. This could be a simple bug, like setting the wrong flag on an API call, or it could be a misunderstanding of how the protections work.

Failures in the platform’s permission models fall into this category. For example, if the app requests too many permissions or the wrong permissions, that is best categorised here.

How Do I Prevent ‘Improper Platform Usage’?
Secure coding and configuration practices must be used on server-side of the mobile application. For specific vulnerability information, refer to the OWASP Web Top Ten or Cloud Top Ten projects.

Example Attack Scenarios
Because there are several platforms, each with hundreds or thousands of APIs, the examples in this section only scratch the surface of what is possible.

App Local Storage Instead of Keychain The iOS Keychain is a secure storage facility for both app and system data. On iOS, apps should use it to store any small data that has security significance (session keys, passwords, device enrolment data, etc.). A common mistake is to store such items in app local storage. Data stored in app local storage is available in unencrypted iTunes backups (e.g., on the user’s computer). For some apps, that exposure is inappropriate.

Below, you can see that there are many risks and vulnerabilities that you must mitigate in order to satisfy M1:

Cloud Top 10 Risks
OWASP Top 10 - 2013

The Worst Offenders Below is a list vulnerability types that OWASP sees most often within mobile applications:

Poor Web Services Hardening
Logic flaws
Testing for business logic flaws
[Business] Logic Security Cheat Sheet](https://www.owasp.org/index.php/Business_Logic_Security_Cheat_Sheet)
Weak Authentication
OWASP Top Ten Broken Authentication Section
Authentication Cheat Sheet
Developers Guide for Authentication
Testing for Authentication
Weak or no session management
Session fixation
Sensitive data transmitted using GET method
Insecure web server configurations
Default content
Administrative interfaces
Injection (SQL, XSS, Command) on both web services and mobile-enabled websites
Authentication flaws
Session Management flaws
Access control vulnerabilities
Local and Remote File Includes
References
OWASP
OWASP Top Ten
External
External References

M2: Insecure Data Storage
Threat Agents
Application Specific

Threats agents include the following: an adversary that has attained a lost/stolen mobile device; malware or another repackaged app acting on the adversary’s behalf that executes on the mobile device.

Attack Vectors
Exploitability EASY

In the event that an adversary physically attains the mobile device, the adversary hooks up the mobile device to a computer with freely available software. These tools allow the adversary to see all third party application directories that often contain stored personally identifiable information (PII) or other sensitive information assets. An adversary may construct malware or modify a legitimate app to steal such information assets.

Security Weakness
Prevalence COMMON
Detectability AVERAGE

Insecure data storage vulnerabilities occur when development teams assume that users or malware will not have access to a mobile device’s filesystem and subsequent sensitive information in data-stores on the device. Filesystems are easily accessible. Organizations should expect a malicious user or malware to inspect sensitive data stores. Usage of poor encryption libraries is to be avoided. Rooting or jailbreaking a mobile device circumvents any encryption protections. When data is not protected properly, specialized tools are all that is needed to view application data.

Technical Impacts
Impact SEVERE

This can result in data loss, in the best case for one user, and in the worst case for many users. It may also result in the following technical impacts: extraction of the app’s sensitive information via mobile malware, modified apps or forensic tools. The nature of the business impact is highly dependent upon the nature of the information stolen. Insecure data may result in the following business impacts:

Identity theft;
Privacy violation;
Fraud;
Reputation damage;
External policy violation (PCI); or
Material loss.
Business Impacts
Application / Business Specific

Insecure data storage vulnerabilities typically lead to the following business risks for the organization that owns the risk app:

Identity Theft
Fraud
Reputation Damage
External Policy Violation (PCI); or
Material Loss.
Am I Vulnerable To ‘Insecure Data Storage’?
This category insecure data storage and unintended data leakage. Data stored insecurely includes, but is not limited to, the following:

SQL databases;
Log files;
XML data stores ou manifest files;
Binary data stores;
Cookie stores;
SD card;
Cloud synced.
Unintended data leakage includes, but is not limited to, vulnerabilities from:

The OS;
Frameworks;
Compiler environment;
New hardware.
Rooted or Jailbroken devices
This is obviously without a developer’s knowledge. In mobile development specifically, this is most seen in undocumented, or under-documented, internal processes such as:

The way the OS caches data, images, key-presses, logging, and buffers;
The way the development framework caches data, images, key-presses, logging, and buffers;
The way or amount of data ad, analytic, social, or enablement frameworks cache data, images, key-presses, logging, and buffers.
How Do I Prevent ‘Insecure Data Storage’?
It is important to threat model your mobile app, OS, platforms and frameworks to understand the information assets the app processes and how the APIs handle those assets. It is crucial to see how they handle the following types of features :

URL caching (both request and response);
Keyboard press caching;
Copy/Paste buffer caching;
Application backgrounding;
Intermediate data
Logging;
HTML5 data storage;
Browser cookie objects;
Analytics data sent to 3rd parties.
Example Attack Scenarios
A Visual Example

iGoat is a purposefully vulnerable mobile app for the security community to explore these types of vulnerabilities first hand. In the exercise below, we enter our credentials and log in to the fake bank app. Then, we navigate to the file system. Within the applications directory, we can see a database called “credentials.sqlite”. Exploring this database reveals that the application is storing our username and credentials (Jason:pleasedontstoremebro!) in plain text.

Local Data Storage Goat Hills Financial Terminal

References
OWASP
OWASP iOS Developer Cheat Sheet
External
Google Androids Developer Security Topics 1
Google Androids Developer Security Topics 2
Apple’s Introduction to Secure Coding
Fortify On Demand Blog - Exploring The OWASP Mobile Top 10: Insecure Data Storage

M3: Insecure Communication
Threat Agents
Application Specific

When designing a mobile application, data is commonly exchanged in a client-server fashion. When the solution transmits its data, it must traverse the mobile device’s carrier network and the internet. Threat agents might exploit vulnerabilities to intercept sensitive data while it’s traveling across the wire. The following threat agents exist:

An adversary that shares your local network (compromised or monitored Wi-Fi);
Carrier or network devices (routers, cell towers, proxy’s, etc); or
Malware on your mobile device.
Attack Vectors
Exploitability EASY

The exploitabilty factor of monitoring a network for insecure communications ranges. Monitoring traffic over a carrier’s network is harder than that of monitoring a local coffee shop’s traffic. In general, targeted attacks are easier to perform.

Security Weakness
Prevalence COMMON
Detectability AVERAGE

Mobile applications frequently do not protect network traffic. They may use SSL/TLS during authentication but not elsewhere. This inconsistency leads to the risk of exposing data and session IDs to interception. The use of transport security does not mean the app has implemented it correctly. To detect basic flaws, observe the phone’s network traffic. More subtle flaws require inspecting the design of the application and the applications configuration.

Technical Impacts
Impact SEVERE

This flaw exposes an individual user’s data and can lead to account theft. If the adversary intercepts an admin account, the entire site could be exposed. Poor SSL setup can also facilitate phishing and MITM attacks.

Business Impacts
Application / Business Specific

At a minimum, interception of sensitive data through a communication channel will result in a privacy violation.

The violation of a user’s confidentiality may result in:

Identity theft;
Fraud, or
Reputational Damage.
Am I Vulnerable To ‘Insecure Communication’?
This risk covers all aspects of getting data from point A to point B, but doing it insecurely. It encompasses mobile-to-mobile communications, app-to-server communications, or mobile-to-something-else communications. This risk includes all communications technologies that a mobile device might use: TCP/IP, WiFi, Bluetooth/Bluetooth-LE, NFC, audio, infrared, GSM, 3G, SMS, etc.

All the TLS communications issues go here. All the NFC, Bluetooth, and WiFi issues go here.

The prominent characteristics include packaging up some kind of sensitive data and transmitting it into or out of the device. Some examples of sensitive data include encryption keys, passwords, private user information, account details, session tokens, documents, metadata, and binaries. The sensitive data can be coming to the device from a server, it can be coming from an app out to a server, or it might be going between the device and something else local (e.g., an NFC terminal or NFC card). The defining characteristic of this risk is the existence of two devices and some data passing between them.

If the data is being stored locally in the device itself, that’s #Insecure Data. If the session details are communicated securely (e.g., via a strong TLS connection) but the session identifer itself is bad (perhaps it is predictable, low entropy, etc.), then that’s an #Insecure Authentication problem, not a communication problem.

The usual risks of insecure communication are around data integrity, data confidentiality, and origin integrity. If the data can be changed while in transit, without the change being detectable (e.g., via a man-in-the-middle attack) then that is a good example of this risk. If confidential data can be exposed, learned, or derived by observing the communications as it happens (i.e., eavesdropping) or by recording the conversation as it happens and attacking it later (offline attack), that’s also an insecure communication problem. Failing to properly setup and validate a TLS connection (e.g., certificate checking, weak ciphers, other TLS configuration problems) are all here in insecure communication.

How Do I Prevent ‘Insecure Communication’?
General Best Practices

Assume that the network layer is not secure and is susceptible to eavesdropping.
Apply SSL/TLS to transport channels that the mobile app will use to transmit sensitive information, session tokens, or other sensitive data to a backend API or web service.
Account for outside entities like third-party analytics companies, social networks, etc. by using their SSL versions when an application runs a routine via the browser/webkit. Avoid mixed SSL sessions as they may expose the user’s session ID.
Use strong, industry standard cipher suites with appropriate key lengths.
Use certificates signed by a trusted CA provider.
Never allow self-signed certificates, and consider certificate pinning for security conscious applications.
Always require SSL chain verification.
Only establish a secure connection after verifying the identity of the endpoint server using trusted certificates in the key chain.
Alert users through the UI if the mobile app detects an invalid certificate.
Do not send sensitive data over alternate channels (e.g, SMS, MMS, or notifications).
If possible, apply a separate layer of encryption to any sensitive data before it is given to the SSL channel. In the event that future vulnerabilities are discovered in the SSL implementation, the encrypted data will provide a secondary defense against confidentiality violation.
Newer threats allow an adversary to eavesdrop on sensitive traffic by intercepting the traffic within the mobile device just before the mobile device’s SSL library encrypts and transmits the network traffic to the destination server. See M10 for more information on the nature of this risk.

iOS Specific Best Practices

Default classes in the latest version of iOS handle SSL cipher strength negotiation very well. Trouble comes when developers temporarily add code to bypass these defaults to accommodate development hurdles. In addition to the above general practices:

Ensure that certificates are valid and fail closed.
When using CFNetwork, consider using the Secure Transport API to designate trusted client certificates. In almost all situations, NSStreamSocketSecurityLevelTLSv1 should be used for higher standard cipher strength.
After development, ensure all NSURL calls (or wrappers of NSURL) do not allow self signed or invalid certificates such as the NSURL class method setAllowsAnyHTTPSCertificate.
Consider using certificate pinning by doing the following: export your certificate, include it in your app bundle, and anchor it to your trust object. Using the NSURL method connection:willSendRequestForAuthenticationChallenge: will now accept your cert.
Android Specific Best Practices

Remove all code after the development cycle that may allow the application to accept all certificates such as org.apache.http.conn.ssl.AllowAllHostnameVerifier or SSLSocketFactory.ALLOW_ALL_HOSTNAME_VERIFIER. These are equivalent to trusting all certificates.
If using a class which extends SSLSocketFactory, make sure checkServerTrusted method is properly implemented so that server certificate is correctly checked.
Example Attack Scenarios
There are a few common scenarios that penetration testers frequently discover when inspecting a mobile app’s communication security:

Lack of certificate inspection

The mobile app and an endpoint successfully connect and perform a TLS handshake to establish a secure channel. However, the mobile app fails to inspect the certificate offered by the server and the mobile app unconditionally accepts any certificate offered to it by the server. This destroys any mutual authentication capability between the mobile app and the endpoint. The mobile app is susceptible to man-in-the-middle attacks through a TLS proxy.

Weak handshake negotiation

The mobile app and an endpoint successfully connect and negotiate a cipher suite as part of the connection handshake. The client successfully negotiates with the server to use a weak cipher suite that results in weak encryption that can be easily decrypted by the adversary. This jeopardizes the confidentiality of the channel between the mobile app and the endpoint.

Privacy information leakage

The mobile app transmits personally identifiable information to an endpoint via non-secure channels instead of over SSL. This jeopardizes the confidentiality of any privacy-related data between the mobile app and the endpoint.

References
OWASP
OWASP
External
External References

M4: Insecure Authentication
Threat Agents
Application Specific

Threat agents that exploit authentication vulnerabilities typically do so through automated attacks that use available or custom-built tools.

Attack Vectors
Exploitability EASY

Once the adversary understands how the authentication scheme is vulnerable, they fake or bypass authentication by submitting service requests to the mobile app’s backend server and bypass any direct interaction with the mobile app. This submission process is typically done via mobile malware within the device or botnets owned by the attacker.

Security Weakness
Prevalence COMMON
Detectability AVERAGE

Poor or missing authentication schemes allow an adversary to anonymously execute functionality within the mobile app or backend server used by the mobile app. Weaker authentication for mobile apps is fairly prevalent due to a mobile device’s input form factor. The form factor highly encourages short passwords that are often purely based on 4-digit PINs. Authentication requirements for mobile apps can be quite different from traditional web authentication schemes due to availability requirements.

In traditional web apps, users are expected to be online and authenticate in real-time with a backend server. Throughout their session, there is a reasonable expectation that they will have continuous access to the Internet.

In mobile apps, users are not expected to be online at all times during their session. Mobile internet connections are much less reliable or predictable than traditional web connections. Hence, mobile apps may have uptime requirements that require offline authentication. This offline requirement can have profound ramifications on things that developers must consider when implementing mobile authentication.

To detect poor authentication schemes, testers can perform binary attacks against the mobile app while it is in ‘offline’ mode. Through the attack, the tester will force the app to bypass offline authentication and then execute functionality that should require offline authentication (for more information on binary attacks, see M10). As well, testers should try to execute any backend server functionality anonymously by removing any session tokens from any POST/GET requests for the mobile app functionality.

Technical Impacts
Impact SEVERE

The technical impact of poor authentication is that the solution is unable to identify the user performing an action request. Immediately, the solution will be unable to log or audit user activity because the identity of the user cannot be established. This will contribute to an inability to detect the source of an attack, the nature of any underlying exploits, or how to prevent future attacks.

Authentication failures may expose underlying authorization failures as well. When authentication controls fail, the solution is unable to verify the user’s identity. This identity is linked to a user’s role and associated permissions. If an attacker is able to anonymously execute sensitive functionality, it highlights that the underlying code is not verifying the permissions of the user issuing the request for the action. Hence, anonymous execution of code highlights failures in both authentication and authorization controls.

Business Impacts
Application / Business Specific

The business impact of poor authentication will typically result in the following at a minimum:

Reputational Damage
Information Theft; or
Unauthorized Access to Data.
Am I Vulnerable To ‘Insecure Authentication’?
There are many different ways that a mobile app may suffer from insecure authentication:

If the mobile app is able to anonymously execute a backend API service request without providing an access token, this application suffers from insecure authentication;
If the mobile app stores any passwords or shared secrets locally on the device, it most likely suffers from insecure authentication;
If the mobile app uses a weak password policy to simplify entering a password, it suffers from insecure authentication; or
If the mobile app uses a feature like TouchID, it suffers from insecure authentication.
How Do I Prevent ‘Insecure Authentication’?
Avoid Weak Patterns

Avoid the following Insecure Mobile Application Authentication Design Patterns:

If you are porting a web application to its mobile equivalent, authentication requirements of mobile applications should match that of the web application component. Therefore, it should not be possible to authenticate with less authentication factors than the web browser;
Authenticating a user locally can lead to client-side bypass vulnerabilities. If the application stores data locally, the authentication routine can be bypassed on jailbroken devices through run-time manipulation or modification of the binary. If there is a compelling business requirement for offline authentication, see M10 for additional guidance on preventing binary attacks against the mobile app;
Where possible, ensure that all authentication requests are performed server-side. Upon successful authentication, application data will be loaded onto the mobile device. This will ensure that application data will only be available after successful authentication;
If client-side storage of data is required, the data will need to be encrypted using an encryption key that is securely derived from the user’s login credentials. This will ensure that the stored application data will only be accessible upon successfully entering the correct credentials. There are additional risks that the data will be decrypted via binary attacks. See M9 for additional guidance on preventing binary attacks that lead to local data theft;
Persistent authentication (Remember Me) functionality implemented within mobile applications should never store a user’s password on the device;
Ideally, mobile applications should utilize a device-specific authentication token that can be revoked within the mobile application by the user. This will ensure that the app can mitigate unauthorized access from a stolen/lost device;
Do not use any spoof-able values for authenticating a user. This includes device identifiers or geo-location;
Persistent authentication within mobile applications should be implemented as opt-in and not be enabled by default;
If possible, do not allow users to provide 4-digit PIN numbers for authentication passwords.
Reinforce Authentication

Developers should assume all client-side authorization and authentication controls can be bypassed by malicious users. Authorization and authentication controls must be re-enforced on the server-side whenever possible.
Due to offline usage requirements, mobile apps may be required to perform local authentication or authorization checks within the mobile app’s code. If this is the case, developers should instrument local integrity checks within their code to detect any unauthorized code changes. See M9 for more information about detecting and reacting to binary attacks.
Example Attack Scenarios
The following scenarios showcase weak authentication or authorization controls in mobile apps:

Scenario #1: Hidden Service Requests: Developers assume that only authenticated users will be able to generate a service request that the mobile app submits to its backend for processing. During the processing of the request, the server code does not verify that the incoming request is associated with a known user. Hence, adversaries submit service requests to the back-end service and anonymously execute functionality that affects legitimate users of the solution.

Scenario #2: Interface Reliance: Developers assume that only authorized users will be able to see the existence of a particular function on their mobile app. Hence, they expect that only legitimately authorized users will be able to issue the request for the service from their mobile device. Back-end code that processes the request does not bother to verify that the identity associated with the request is entitled to execute the service. Hence, adversaries are able to perform remote administrative functionality using fairly low-privilege user accounts.

Scenario #3: Usability Requirements: Due to usability requirements, mobile apps allow for passwords that are 4 digits long. Server code correctly stores a hashed version of the password. However, due to the severely short length of the password, an adversary will be able to quickly deduce the original passwords using rainbow hash tables. If the password file (or data store) on the server is compromised, an adversary will be able to quickly deduce users’ passwords.

References
OWASP
OWASP
External
External References

M5: Insufficient Cryptography
Threat Agents
Application Specific

Threat agents include the following: anyone with physical access to data that has been encrypted improperly, or mobile malware acting on an adversary’s behalf.

Attack Vectors
Exploitability EASY

The attack vectors correspond to the same attack vectors available through the traditional OWASP Top Ten. Any exposed API call can serve as attack vector here.

Security Weakness
Prevalence COMMON
Detectability AVERAGE

In order to exploit this weakness, an adversary must successfully return encrypted code or sensitive data to its original unencrypted form due to weak encryption algorithms or flaws within the encryption process.

Technical Impacts
Impact SEVERE

This vulnerability will result in the unauthorized retrieval of sensitive information from the mobile device.

Business Impacts
Application / Business Specific

This vulnerability can have a number of different business impacts. Typically, broken cryptography will result in the following:

Privacy Violations;
Information Theft;
Code Theft;
Intellectual Property Theft; or
Reputational Damage.
Am I Vulnerable To ‘Insufficient Cryptography’?
Insecure use of cryptography is common in most mobile apps that leverage encryption. There are two fundamental ways that broken cryptography is manifested within mobile apps. First, the mobile app may use a process behind the encryption / decryption that is fundamentally flawed and can be exploited by the adversary to decrypt sensitive data. Second, the mobile app may implement or leverage an encryption / decryption algorithm that is weak in nature and can be directly decrypted by the adversary. The following subsections explore both of these scenarios in more depth:

Reliance Upon Built-In Code Encryption Processes
By default, iOS applications are protected (in theory) from reverse engineering via code encryption. The iOS security model requires that apps be encrypted and signed by trustworthy sources in order to execute in non-jailbroken environments. Upon start-up, the iOS app loader will decrypt the app in memory and proceed to execute the code after its signature has been verified by iOS. This feature, in theory, prevents an attacker from conducting binary attacks against an iOS mobile app.

Using freely available tools like ClutchMod or GBD, an adversary will download the encrypted app onto their jailbroken device and take a snapshot of the decrypted app once the iOS loader loads it into memory and decrypts it (just before the loader kicks off execution). Once the adversary takes the snapshot and stores it on disk, the adversary can use tools like IDA Pro or Hopper to easily perform static / dynamic analysis of the app and conduct further binary attacks.

Bypassing built-in code encryption algorithms is trivial at best. Always assume that an adversary will be able to bypass any built-in code encryption offered by the underlying mobile OS. For more information about additional steps you can take to provide additional layers of reverse engineering prevention, see M9.

Poor Key Management Processes

The best algorithms don’t matter if you mishandle your keys. Many make the mistake of using the correct encryption algorithm, but implementing their own protocol for employing it. Some examples of problems here include:

Including the keys in the same attacker-readable directory as the encrypted content;
Making the keys otherwise available to the attacker;
Avoid the use of hardcoded keys within your binary; and
Keys may be intercepted via binary attacks. See M10 for more information on preventing binary attacks.
Creation and Use of Custom Encryption Protocols

There is no easier way to mishandle encryption–mobile or otherwise–than to try to create and use your own encryption algorithms or protocols.

Always use modern algorithms that are accepted as strong by the security community, and whenever possible leverage the state of the art encryption APIs within your mobile platform. Binary attacks may result in adversary identifying the common libraries you have used along with any hardcoded keys in the binary. In cases of very high security requirements around encryption, you should strongly consider the use of whitebox cryptography. See M10 for more information on preventing binary attacks that could lead to the exploitation of common libraries.

Use of Insecure and/or Deprecated Algorithms

Many cryptographic algorithms and protocols should not be used because they have been shown to have significant weaknesses or are otherwise insufficient for modern security requirements. These include:

RC2
MD4
MD5
SHA1
How Do I Prevent ‘Insufficient Cryptography’?
It is best to do the following when handling sensitive data:

Avoid the storage of any sensitive data on a mobile device where possible.
Apply cryptographic standards that will withstand the test of time for at least 10 years into the future; and
Follow the NIST guidelines on recommended algorithms (see external references).
Example Attack Scenarios
None

References
OWASP
OWASP Cryptographic Storage Cheat Sheet
OWASP Key Management Cheat Sheet
External
NIST Encryption Guidelines

M6: Insecure Authorization
Threat Agents
Application Specific

Threat agents that exploit authorization vulnerabilities typically do so through automated attacks that use available or custom-built tools.

Attack Vectors
Exploitability EASY

Once the adversary understands how the authorization scheme is vulnerable, they login to the application as a legitimate user. They successfully pass the authentication control. Once past authentication, they typically force-browse to a vulnerable endpoint to execute administrative functionality. This submission process is typically done via mobile malware within the device or botnets owned by the attacker.

Security Weakness
Prevalence COMMON
Detectability AVERAGE

To test for poor authorization schemes, testers can perform binary attacks against the mobile app and try to execute privileged functionality that should only be executable with a user of higher privilege while the mobile app is in ‘offline’ mode (for more information on binary attacks, see M9 and M10). As well, testers should try to execute any privileged functionality using a low-privilege session token within the corresponding POST/GET requests for the sensitive functionality to the backend server.Poor or missing authorization schemes allow an adversary to execute functionality they should not be entitled to using an authenticated but lower-privilege user of the mobile app. Authorization requirements are more vulnerable when making authorization decisions within the mobile device instead of through a remote server. This may be a requirement due to mobile requirements of offline usability.

Technical Impacts
Impact SEVERE

The technical impact of poor authorization is similar in nature to the technical impact of poor authentication. The technical impact can be wide ranging in nature and dependent upon the nature of the over-privileged functionality that is executed. For example, over-privileged execution of remote or local administration functionality may result in destruction of systems or access to sensitive information.

Business Impacts
Application / Business Specific

In the event that a user (anonymous or verified) is able to execute over-privileged functionality, the business may experience the following impacts:

Reputational Damage;
Fraud; or
Information Theft.
Am I Vulnerable To ‘Insecure Authorization’?
It is important to recognize the difference between authentication and authorization. Authentication is the act of identifying an individual. Authorization is the act of checking that the identified individual has the permissions necessary to perform the act. The two are closely related as authorization checks should always immediately follow authentication of the an incoming request from a mobile device.

If an organization fails to authenticate and individual before executing an API endpoint requested from a mobile device, then the code automatically suffers from insecure authorization as well. It is essentially impossible for authorization checks to occur on an incoming request when the caller’s identity is not established.

There are a few easy rules to follow when trying to determine if a mobile endpoint is suffering from insecure authorization:

Presence of Insecure Direct Object Reference (IDOR) vulnerabilities - If you are seeing an Insecure Direct Object Reference Vulnerability (IDOR), the code is most likely not performing a valid authorization check; and
Hidden Endpoints - Typically, developers do not perform authorization checks on backend hidden functionality as they assume the hidden functionality will only be seen by someone in the right role;
User Role or Permission Transmissions - If the mobile app is transmitting the user’s roles or permissions to a backend system as part of a request, it is suffering from insecure authorization.
How Do I Prevent ‘Insecure Authorization’?
In order to avoid insecure authorization checks, do the following:

Verify the roles and permissions of the authenticated user using only information contained in backend systems. Avoid relying on any roles or permission information that comes from the mobile device itself;
Backend code should independently verify that any incoming identifiers associated with a request (operands of a requested operation) that come along with the identify match up and belong to the incoming identity;
Example Attack Scenarios
Scenario #1: Insecure Direct Object Reference:

A user makes an API endpoint request to a backend REST API that includes an actor ID and an oAuth bearer token. The user includes their actor ID as part of the incoming URL and includes the access token as a standard header in the request. The backend verifies the presence of the bearer token but fails to validate the actor ID associated with the bearer token. As a result, the user can tweak the actor ID and attain account information of other users as part of the REST API request.

Scenario #2: Transmission of LDAP roles:

A user makes an API endpoint request to a backend REST API that includes a standard oAuth bearer token along with a header that includes a list of LDAP groups that the user belongs to. The backend request validates the bearer token and then inspects the incoming LDAP groups for the right group membership before continuing on to the sensitive functionality. However, the backend system does not perform an independent validation of LDAP group membership and instead relies upon the incoming LDAP information coming from the user. The user can tweak the incoming header and report to be a member of any LDAP group arbitrarily and perform administrative functionality.

References
OWASP
OWASP
External
External References

M7: Poor Code Quality
Threat Agents
Application Specific

Threat Agents include entities that can pass untrusted inputs to method calls made within mobile code. These types of issues are not necessarily security issues in and of themselves but lead to security vulnerabilities. For example, buffer overflows within older versions of Safari (a poor code quality vulnerability) led to high risk drive-by Jailbreak attacks. Poor code-quality issues are typically exploited via malware or phishing scams.

Attack Vectors
Exploitability DIFFICULT

An attacker will typically exploit vulnerabilities in this category by supplying carefully crafted inputs to the victim. These inputs are passed onto code that resides within the mobile device where exploitation takes place. Typical types of attacks will exploit memory leaks and buffer overflows.

Security Weakness
Prevalence COMMON
Detectability DIFFICULT

Code quality issues are fairly prevalent within most mobile code. The good news is that most code quality issues are fairly benign and result in bad programming practice. It is typically difficult to detect these types of issues through manual code review. Instead, attackers will use third-party tools that perform static analysis or perform fuzzing. These types of tools will typically identify memory leaks, buffer overflows, and other less severe issues that result in bad programming practice. Hackers with extreme low-level knowledge and expertise are able to effectively exploit these types of issues. The typical primary goal is to execute foreign code within the mobile code’s address space.

Technical Impacts
Impact MODERATE

Most exploitations that fall into this category result in foreign code execution or denial of service on remote server endpoints (and not the mobile device itself). However, in th event that buffer overflows/overruns do exist within the mobile device and the input can be derived from an external party, this could have a severely high technical impact and should be remediated.

Business Impacts
Application / Business Specific

The business impact from this category of vulnerabilities varies greatly, depending upon the nature of the exploit. Poor code quality issues that result in remote code execution could lead to the following business impacts:

Information Theft;
Reputational Damage;
Intellectual Property Theft
Other less severe technical issues that fall into this category may lead to degradations in performance, memory usage, or poor front-end architecture.

Am I Vulnerable To ‘Poor Code Quality’?
This is the catch-all for code-level implementation problems in the mobile client. That’s distinct from server-side coding mistakes. This captures the risks that come from vulnerabilities like buffer overflows, format string vulnerabilities, and various other code-level mistakes where the solution is to rewrite some code that’s running on the mobile device.

This is distinct from Improper Platform Usage because it usually refers to the programming language itself (e.g., Java, Swift, Objective C, JavaScript). A buffer overflow in C or a DOM-based XSS in a Webview mobile app would be code quality issues.

The key characteristic of this risk is that it’s code executing on the mobile device and the code needs to be changed in a fairly localised way. Fixing most risks requires code changes, but in the code quality case the risk comes from using the wrong API, using an API insecurely, using insecure language constructs, or some other code-level issue. Importantly: this is not code running on the server. This is a risk that captures bad code that executes on the mobile device itself.

How Do I Prevent ‘Poor Code Quality’?
In general, code quality issues can be avoided by doing the following:

Maintain consistent coding patterns that everyone in the organization agrees upon;
Write code that is easy to read and well-documented;
When using buffers, always validate that the the lengths of any incoming buffer data will not exceed the length of the target buffer;
Via automation, identify buffer overflows and memory leaks through the use of third-party static analysis tools; and
Prioritize solving buffer overflows and memory leaks over other ‘code quality’ issues.
Example Attack Scenarios
Scenario #1: Buffer Overflow example:

include <stdio.h>

 int main(int argc, char **argv)
 {
    char buf[8]; // buffer for eight characters
    gets(buf); // read from stdio (sensitive function!)
    printf("%s\n", buf); // print out data stored in buf
    return 0; // 0 as return value
 }
In this example, taken from this page, we should avoid the use of the gets function to avoid a buffer overflow. This is an example of what most static analysis tools will report as a code quality issue.

References
OWASP
Buffer Overflow Examples
External
External References

M8: Code Tampering
Threat Agents
Application Specific

Typically, an attacker will exploit code modification via malicious forms of the apps hosted in third-party app stores. The attacker may also trick the user into installing the app via phishing attacks.

Attack Vectors
Exploitability EASY

Typically, an attacker will do the following things to exploit this category:

Make direct binary changes to the application package’s core binary
Make direct binary changes to the resources within the application’s package
Redirect or replace system APIs to intercept and execute foreign code that is malicious
Security Weakness
Prevalence COMMON
Detectability AVERAGE

Modified forms of applications are surprisingly more common than you think. There is an entire security industry built around detecting and removing unauthorized versions of mobile apps within app stores. Depending upon the approach taken to solving the problem of detecting code modification, organizations can have limited to highly successful ways of detecting unauthorized versions of code in the wild. This category covers binary patching, local resource modification, method hooking, method swizzling, and dynamic memory modification.

Once the application is delivered to the mobile device, the code and data resources are resident there. An attacker can either directly modify the code, change the contents of memory dynamically, change or replace the system APIs that the application uses, or modify the application’s data and resources. This can provide the attacker a direct method of subverting the intended use of the software for personal or monetary gain.

Technical Impacts
Impact SEVERE

The impact from code modification can be wide ranging in nature, depending upon the nature of the modification itself. Typical types of impacts include the following:

Unauthorized new features;
Identity theft; or
Fraud.
Business Impacts
Application / Business Specific

The business impact from code modification typically results in the following:

Revenue loss due to piracy; or
Reputational damage.
Am I Vulnerable To ‘Code Tampering’?
Technically, all mobile code is vulnerable to code tampering. Mobile code runs within an environment that is not under the control of the organization producing the code. At the same time, there are plenty of different ways of altering the environment in which that code runs. These changes allow an adversary to tinker with the code and modify it at will.

Although mobile code is inherently vulnerable, it is important to ask yourself if it is worth detecting and trying to prevent unauthorized code modification. Apps written for certain business verticals (gaming for example) are much more vulnerable to the impacts of code modification than others (hospitality for example). As such, it is critical to consider the business impact before deciding whether or not to address this risk.

How Do I Prevent ‘Code Tampering’?
The mobile app must be able to detect at runtime that code has been added or changed from what it knows about its integrity at compile time. The app must be able to react appropriately at runtime to a code integrity violation.

The remediation strategies for this type of risk is outlined in more technical detail within the OWASP Reverse Engineering and Code Modification Prevention Project.

Android Root Detection Typically, an app that has been modified will execute within a Jailbroken or rooted environment. As such, it is reasonable to try and detect these types of compromised environments at runtime and react accordingly (report to the server or shutdown). There are a few common ways to detect a rooted Android device: Check for test-keys

Check to see if build.prop includes the line ro.build.tags=test-keys indicating a developer build or unofficial ROM
Check for OTA certificates

Check to see if the file /etc/security/otacerts.zip exists
Check for several known rooted apk’s

com.noshufou.android.su
com.thirdparty.superuser
eu.chainfire.supersu
com.koushikdutta.superuser
Check for SU binaries

/system/bin/su
/system/xbin/su
/sbin/su
/system/su
/system/bin/.ext/.su
Attempt SU command directly

Attempt the to run the command su and check the id of the current user, if it returns 0 then the su command has been successful
iOS Jailbreak Detection

Example Attack Scenarios
There are a number of counterfeit applications that are available across the app stores. Some of these contain malware payloads. Many of the modified apps contain modified forms of the original core binary and associated resources. The attacker re-packages these as a new application and released them into third-party stores.

Scenario #1:

Games are a particularly popular target to attack using this method. The attacker will attract people that are not interested in paying for any freemium features of the game. Within the code, the attacker short-circuits conditional jumps that detect whether an in-application purchase is successful. This bypass allows the victim to attain game artifacts or new abilities without paying for them. The attacker has also inserted spyware that will steal the identity of the user.

Scenario #2:

Banking apps are another popular target to attack. These apps typically process sensitive information that will be useful to an attacker. An attacker could create a counterfeit version of the app that transmits the user’s personally identifiable information (PII) along with username/password to a third-party site. This is reminiscent of the desktop equivalent of Zeus malware. This typically results in fraud against the bank.

References
OWASP
OWASP Reverse Engineering and Code Modification Prevention Project
External
OWASP
OWASP Reverse Engineering and Code Modification Prevention Project
External

[1] Arxan Research: State of Security in the App Economy, Volume 2, November 2013:
“Adversaries have hacked 78 percent of the top 100 paid Android and iOS apps in 2013.”

[2] HP Research: HP Research Reveals Nine out of 10 Mobile Applications Vulnerable to Attack, 18 November 2013:
“86 percent of applications tested lacked binary hardening, leaving applications vulnerable to information disclosure, buffer overflows and poor performance. To ensure security throughout the life cycle of the application, it is essential to build in the best security practices from conception.”

[3] North Carolina State University: Dissecting Android Malware: Characterization and Evolution, 7 September 2011:
“Our results show that 86.0% of them (Android Malware) repackage legitimate apps to include malicious payloads; 36.7% contain platform-level exploits to escalate privilege; 93.0% exhibit the bot-like capability.”

[4] Tech Hive: Apple Pulls Ripoff Apps from its Walled Garden Feb 4th, 2012:
“While Apple is known for screening apps before they are allowed to sprout up in its walled garden, clearly fake apps do get in. Once they do, getting them out depends on developers who raise a fuss.”

[5] Tech Crunch: Developer Spams Google Play With RipOffs of Well-Known Apps… Again, January 2 2014:
“It’s not uncommon to search the Google Play app store and find a number of knock-off or “fake” apps aiming to trick unsuspecting searchers into downloading them over the real thing.”

[6] Extreme Tech: Chinese App Store Offers Pirated iOS Apps Without the Need To Jailbreak, April 19 2013:
“The site offers apps for free that would otherwise cost money, including big-name titles.”

[7] OWASP: Architectural Principles That Prevent Code Modification or Reverse Engineering, January 11th 2014.

[8] Gartner report: Avoiding Mobile App Development Security Pitfalls, 24 May 2013:

“For critical applications, such as transactional ones and sensitive enterprise applications, hardening should be used.”

[9] Gartner report: Emerging Technology Analysis: Mobile Application Shielding, March 26th, 2013:
“As more regulated and sensitive data applications move to mobile platforms the need to increase data protection increases. Mobile application shielding presents the opportunity to security providers to offer higher data protection standards to mobile platforms that exceed mobile OS security.”

[10] Gartner report: Proliferating Mobile Transaction Attack Vectors and What to Do About Them, March 1st, 2013:
“Use mobile application security testing services and self-defending application utilities to help prevent hacking attempts.”

[11] Gartner report: Select a Secure Mobile Wallet for Proximity, March 1st, 2013:
“Application hardening can fortify sensitive business code against hacking attempts, such as reverse engineering”

[12] Forrester paper: Choose The Right Mobile Development Solutions For Your Organization, May 6th 2013:
“5 Key Protections: Data Protection, App Compliance, App-Level Threat Defense, Security Policy Enforcement, App Integrity”

[13] John Wiley and Sons, Inc: iOS Hacker’s Handbook, Published May 2012, ISBN 1118204123.

[14] McGraw Hill Education: Mobile Hacking Exposed, Published July 2013, ISBN 0071817018.

[15] Publisher Unannounced: Android Hacker’s Handbook, To Be Published April 2014.

[16] Software Development Times: More than 5,000 apps in the Google Play Store are copied APKs, or ‘thief-ware’, November 20 2013:

“In most cases, the 2,140 copycat developers that were found reassembled the apps almost identically, adding new advertising SDKs to siphon profits away from the original developers.

[17] InfoSecurity Magazine: Two Thirds of Personal Banking Apps Found Full of Vulnerabilities, January 3 2014:
“But one of his more worrying findings came from disassembling the apps themselves … what he found was hardcoded development credentials within the code. An attacker could gain access to the development infrastructure of the bank and infest the application with malware causing a massive infection for all of the application’s users.”

[18] InfoSecurity Magazine: Mobile Malware Infects Millions; LTE Spurs Growth, January 29 2014:
“Number of mobile malware samples is growing at a rapid clip, increasing by 20-fold in 2013… It is trivial for an attacker to hijack a legitimate Android application, inject malware into it and redistribute it for consumption. There are now binder kits available that will allow an attacker to automatically inject malware into an existing application”

M9: Reverse Engineering
Threat Agents
Application Specific

An attacker will typically download the targeted app from an app store and analyze it within their own local environment using a suite of different tools.

Attack Vectors
Exploitability EASY

An attacker must perform an analysis of the final core binary to determine its original string table, source code, libraries, algorithms, and resources embedded within the app. Attackers will use relatively affordable and well-understood tools like IDA Pro, Hopper, otool, strings, and other binary inspection tools from within the attacker’s environment.

Security Weakness
Prevalence COMMON
Detectability EASY

Generally, all mobile code is susceptible to reverse engineering. Some apps are more susceptible than others. Code written in languages / frameworks that allow for dynamic introspection at runtime (Java, .NET, Objective C, Swift) are particularly at risk for reverse engineering. Detecting susceptibility to reverse engineering is fairly straight forward. First, decrypt the app store version of the app (if binary encryption is applied). Then, use the tools outlined in the “Attack Vectors” section of this document against the binary. Code will be susceptible if it is fairly easy to understand the app’s controlflow path, string table, and any pseudocode/source-code generated by these tools.

Technical Impacts
Impact Moderate

An attacker may exploit reverse engineering to achieve any of the following:

Reveal information about back end servers;
Reveal cryptographic constants and ciphers;
Steal intellectual property;
Perform attacks against back end systems; or
Gain intelligence needed to perform subsequent code modification.
Business Impacts
Application / Business Specific

The business impacts from reverse engineering are quite varied. They include the following:

Intellectual Property theft;
Reputational Damage;
Identity Theft; or
Compromise of Backend Systems.
Am I Vulnerable To ‘Reverse Engineering’?
Generally, most applications are susceptible to reverse engineering due to the inherent nature of code. Most languages used to write apps today are rich in metadata that greatly aides a programmer in debugging the app. This same capability also grealy aides an attacker in understanding how the app works. An app is said to be susceptible to reverse engineering if an attacker can do any of the following things:

Clearly understand the contents of a binary’s string table
Accurately perform cross-functional analysis
Derive a reasonably accurate recreation of the source code from the binary Although most apps are susceptible to reverse engineering, it’s important to examine the potential business impact of reverse engineering when considering whether or not to mitigate this risk. See the examples below for a small sampling of what can be done with reverse engineering on its own.
How Do I Prevent ‘Reverse Engineering’?
In order to prevent effective reverse engineering, you must use an obfuscation tool. There are many free and commercial grade obfuscators on the market. Conversely, there are many different deobfuscators on the market. To measure the effectiveness of whatever obfuscation tool you choose, try deobfuscating the code using tools like IDA Pro and Hopper.

A good obfuscator will have the following abilities:

Narrow down what methods / code segments to obfuscate;
Tune the degree of obfuscation to balance performance impact;
Withstand de-obfuscation from tools like IDA Pro and Hopper;
Obfuscate string tables as well as methods
Example Attack Scenarios
Scenario #1: String Table Analysis:

The attacker runs ‘strings’ against the unencrypted app. As a result of the string table analysis, the attacker discovers a hardcoded connectivity string that contains authentication credentials to a backend database. The attacker uses those credentials to gain access to the database. The attacker steals a vast array of PII data about the app’s users.

Scenario #2: Cross-Functional Analysis:

The attacker uses IDA Pro against an unencrypted app. As a result of the string table analysis combined with functioanl cross-referencing, the attacker discovers Jailbreak detection code. The attacker uses this knowledge in a subequent code-modification attack to disable jailbreak detection within the mobile app. The attacker then deploys a version of the app that exploits method swizzling to steal customer information.

Scenario #3: Source Code Analysis:

Consider a banking Android application. The APK file can be easily extracted using 7zip/Winrar/WinZip/Gunzip. Once extracted, the attacker has manifest file, assets, resources and most importantly classes.dex file.

Then using Dex to Jar converter, an attacker can easily convert it to jar file. In next step, Java Decompiler (like JDgui) will provide you the code.

References
OWASP
OWASP Reverse Engineering and Code Modification Prevention Project
External

[1] Arxan Research: State of Security in the App Economy, Volume 2, November 2013:
“Adversaries have hacked 78 percent of the top 100 paid Android and iOS apps in 2013.”

[2] HP Research: HP Research Reveals Nine out of 10 Mobile Applications Vulnerable to Attack, 18 November 2013:
“86 percent of applications tested lacked binary hardening, leaving applications vulnerable to information disclosure, buffer overflows and poor performance. To ensure security throughout the life cycle of the application, it is essential to build in the best security practices from conception.”

[3] North Carolina State University: Dissecting Android Malware: Characterization and Evolution, 7 September 2011:
“Our results show that 86.0% of them (Android Malware) repackage legitimate apps to include malicious payloads; 36.7% contain platform-level exploits to escalate privilege; 93.0% exhibit the bot-like capability.”

[4] Tech Hive: Apple Pulls Ripoff Apps from its Walled Garden Feb 4th, 2012:
“While Apple is known for screening apps before they are allowed to sprout up in its walled garden, clearly fake apps do get in. Once they do, getting them out depends on developers who raise a fuss.”

[5] Tech Crunch: Developer Spams Google Play With RipOffs of Well-Known Apps… Again, January 2 2014:
“It’s not uncommon to search the Google Play app store and find a number of knock-off or “fake” apps aiming to trick unsuspecting searchers into downloading them over the real thing.”

[6] Extreme Tech: Chinese App Store Offers Pirated iOS Apps Without the Need To Jailbreak, April 19 2013:
“The site offers apps for free that would otherwise cost money, including big-name titles.”

[7] OWASP: Architectural Principles That Prevent Code Modification or Reverse Engineering, January 11th 2014.

[8] Gartner report: Avoiding Mobile App Development Security Pitfalls, 24 May 2013:

“For critical applications, such as transactional ones and sensitive enterprise applications, hardening should be used.”

[9] Gartner report: Emerging Technology Analysis: Mobile Application Shielding, March 26th, 2013:
“As more regulated and sensitive data applications move to mobile platforms the need to increase data protection increases. Mobile application shielding presents the opportunity to security providers to offer higher data protection standards to mobile platforms that exceed mobile OS security.”

[10] Gartner report: Proliferating Mobile Transaction Attack Vectors and What to Do About Them, March 1st, 2013:
“Use mobile application security testing services and self-defending application utilities to help prevent hacking attempts.”

[11] Gartner report: Select a Secure Mobile Wallet for Proximity, March 1st, 2013:
“Application hardening can fortify sensitive business code against hacking attempts, such as reverse engineering”

[12] Forrester paper: Choose The Right Mobile Development Solutions For Your Organization, May 6th 2013:
“5 Key Protections: Data Protection, App Compliance, App-Level Threat Defense, Security Policy Enforcement, App Integrity”

[13] John Wiley and Sons, Inc: iOS Hacker’s Handbook, Published May 2012, ISBN 1118204123.

[14] McGraw Hill Education: Mobile Hacking Exposed, Published July 2013, ISBN 0071817018.

[15] Publisher Unannounced: Android Hacker’s Handbook, To Be Published April 2014.

[16] Software Development Times: More than 5,000 apps in the Google Play Store are copied APKs, or ‘thief-ware’, November 20 2013:

“In most cases, the 2,140 copycat developers that were found reassembled the apps almost identically, adding new advertising SDKs to siphon profits away from the original developers.

[17] InfoSecurity Magazine: Two Thirds of Personal Banking Apps Found Full of Vulnerabilities, January 3 2014:
“But one of his more worrying findings came from disassembling the apps themselves … what he found was hardcoded development credentials within the code. An attacker could gain access to the development infrastructure of the bank and infest the application with malware causing a massive infection for all of the application’s users.”

[18] InfoSecurity Magazine: Mobile Malware Infects Millions; LTE Spurs Growth, January 29 2014:
“Number of mobile malware samples is growing at a rapid clip, increasing by 20-fold in 2013… It is trivial for an attacker to hijack a legitimate Android application, inject malware into it and redistribute it for consumption. There are now binder kits available that will allow an attacker to automatically inject malware into an existing application”

M10: Extraneous Functionality
Threat Agents
Application Specific

Typically, an attacker seeks to understand extraneous functionality within a mobile app in order to discover hidden functionality in in backend systems. The attacker will typically exploit extraneous functionality directly from their own systems without any involvement by end-users.

Attack Vectors
Exploitability EASY

An attacker will download and examine the mobile app within their own local environment. They will examine log files, configuration files, and perhaps the binary itself to discover any hidden switches or test code that was left behind by the developers. They will exploit these switches and hidden functionality in the backend system to perform an attack.

Security Weakness
Prevalence COMMON
Detectability AVERAGE

There is a high likelihood that any given mobile app contains extraneous functionality that is not directly exposed to the user via the interface. Most of this additional code is benign in nature and will not give an attacker any additional insight into backend capabilities. However, some extraneous functionality can be very useful to an attacker. Functionality that exposes information related to back-end test, demo, staging, or UAT environments should not be included in a production build. Additionally, administrative API endpoints, or unofficial endpoints should not be included in final production builds. Detecting extraneous functionality can be tricky. Automated static and dynamic analysis tools can pick up low hanging fruit (log statements). However, some backdoors are difficult to detect in an automated means. As such, it is always best to prevent these things using a manual code review.

Technical Impacts
Impact SEVERE

The technical impact from extraneous functionality includes the following:

Exposure of how backend systems work; or
Unauthorized high-privileged actions executed.
Business Impacts
Application / Business Specific

The business impact from extraneous functionality includes the following:

Unauthorized Access to Sensitive Functionality;
Reputational Damage; or
Intellectual Property Theft.
Am I Vulnerable To ‘Extraneous Functionality’?
Often, developers include hidden backdoor functionality or other internal development security controls that are not intended to be released into a production environment. For example, a developer may accidentally include a password as a comment in a hybrid app. Another example includes disabling of 2-factor authentication during testing.

The defining characteristic of this risk is leaving functionality enabled in the app that was not intended to be released.

How Do I Prevent ‘Extraneous Functionality’?
The best way to prevent this vulnerability is to perform a manual secure code review using security champs or subject matter experts most knowledgable with this code. They should do the following:

Examine the app’s configuration settings to discover any hidden switches;
Verify that all test code is not included in the final production build of the app;
Examine all API endpoints accessed by the mobile app to verify that these endpoints are well documented and publicly available;
Examine all log statements to ensure nothing overly descriptive about the backend is being written to the logs;
Example Attack Scenarios
Scenario #1: Administrative Endpoint Exposed:

As part of mobile endpoint testing, developers included a hidden interface within the mobile app that would display an administrative dashboard. This dashboard accessed admin information via the back-end API server. In the production version of the code, the developers did not include code that displayed the dashboard at any time. However, they did include the underlying code that could access the back-end admin API. An attacker performed a string table analysis of the binary and discovered the hardcoded URL to an administrative REST endpoint. The attacker subsequently used ‘curl’ to execute back-end administrative functionality.

The developers should have removed all extraneous code, including code that is not directly reachable by the native interface.

Scenario #2: Debug Flag in Configuration File:

An attacker tries manually added “debug=true” to a .properties file in a local app. Upon startup, the application is outputting log files that are overly descriptive and helpful to the attacker in understanding the backend systems. The attacker subsequently discovers vulnerabilities within the backend system as a result of the log.

The developers should have prevented the activation of ‘debug mode’ within a production build of the mobile app.

References
OWASP
OWASP
External
External References