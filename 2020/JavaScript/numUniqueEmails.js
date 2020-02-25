// Every email consists of a local name and a domain name, separated by the @ sign.
// For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.
// Besides lowercase letters, these emails may contain '.'s or '+'s.
// If you add periods ('.') between some characters in the local name part of an email address, 
// mail sent there will be forwarded to the same address without dots in the local name.  
// For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  
// (Note that this rule does not apply for domain names.)
// If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. 
// This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  
// (Again, this rule does not apply for domain names.)
// It is possible to use both of these rules at the same time.
// Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 

// Example 1:
// Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
// Output: 2
// Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails

const numUniqueEmails = function(emails) {
    let cleanEmails = []
    for (let i = 0; i < emails.length; i++) {
        let arr = emails[i].split("@")
        let local = arr[0]
        let j = 0
        while (local.includes('.')) {
            if (local[j] === '.') {
                local = local.slice(0,j) + local.slice(j+1)
                j --
            } else {
                j ++
            }
        }
        if (local.includes('+')) {
            let idxPlus = local.indexOf('+')
            local = local.slice(0,idxPlus)
        }
        let domain = arr[1]
        let cleanEmail = local + '@' + domain
        if (cleanEmails.includes(cleanEmail)) {

        } else {
            cleanEmails.push(cleanEmail)
        }
    }
    console.log(cleanEmails)
    return cleanEmails.length
}

console.log(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))