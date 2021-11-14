


INSERT INTO `EventsTypes` (`label`, `description`, `requirements`) VALUES
('Information Session', 'In this event, a mental health professional will give a presentation on a specific topic.', 'At least one mental health professional is needed for this event.'),
('Community Building Event', 'This social event will help the surrounding community get to know each other and encourage unity among neighbors.', 'None.'),
('Mental Health Professionals Social', 'This will be a come and go event in which many mental health professionals will meet the community members and help destigmatize mental health issues.', 'Multiple mental health professionals are needed for this event.');


INSERT INTO `Events` (`address`, `city`, `state`, `EventsTypes.id`, `reason`, `time`, `zip`, `description`) VALUES
('', 'San Francisco', 'CA', 2, 'Our city has been impacted due to COVID-19 and we believe this will help reunite our community.', '2021-11-25 10:00:00', '86753', 'This event will consist of a large gathering of members from the community in a stress free setting to reconnect and encourage others to reach out to get help for mental health care issues if they need it.'),
('', 'New York', 'TX', 1, 'We feel it could benefit the community', '2021-12-29 14:00:00', '98765', 'Discussions on anxiety, depression, and how to best recognize their signs and combat them. Resources for attendees or attendees who know people struggling with this issue will be available. Those who have experience with these issues will have open opportunities to talk about their stories and ask questions.'),
('', 'Dubuque', 'IA', 3, 'Our counselors have reported that their clients had struggled to find counselors that fit.', '2022-1-5 16:00:00', '19537', 'We will host many different mental health care professionals from nearby practices in community centers to provide their contact information to the town and encourage them to get the help they need.');


INSERT INTO `Counselors` (`description`, `education`, `name`, `practice`, `specialties`, `title`) VALUES
('Passionate about age 8-18, emerging adults & young professionals.', 'UT Dallas', 'Jake from State Farm', 'Counseling 123', 'Eating issues, athletic performance, body image, mood concerns, immigrant & 2nd generation struggles, & Adult Children of Alcoholics/Addicts', 'LPC'),
('Warm & compassionate - Whitney works with all ages on resilience and long-term healing.', 'Texas A&M', 'Whitney Lander', 'Happy Place', 'New mothers, parenting dynamics, couples & all humans who are looking to become better versions of themselves', 'LPC, ATR'),
('Passionate about teens, emerging adults and young professionals. ', 'SMU', 'Jackson Legacy', 'Happy Place', 'Anxiety, depression, trauma, relationship issues, self-esteem, emotional regulation, distress tolerance, and eating/body concerns', 'LCSW'),
('Sarah brings humor and authenticity to her work with emerging adults, kids, teens & families. With more than 30 years of experience, she is a wise guide to help you thrive in life and relationships.', 'UT Austin', 'Sarah Peters', 'Counseling 123', 'Trauma, life transitions, anxiety, depression, parenting, and adult children of parents with personality disorders', 'LPC Associate');


INSERT INTO `EventsCounselors` (`Counselors.id`, `Events.id`) VALUES
(1, 1),
(1, 3),
(2, 3),
(3, 3),
(4, 3);


