-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 31, 2024 at 04:22 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mental_thrive`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_portal`
--

CREATE TABLE `admin_portal` (
  `id` int(255) NOT NULL,
  `Aemail` varchar(255) NOT NULL,
  `Apassword` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_portal`
--

INSERT INTO `admin_portal` (`id`, `Aemail`, `Apassword`) VALUES
(2, 'mima@phinmaed.com', 'mima123!');

-- --------------------------------------------------------

--
-- Table structure for table `counselor_portal`
--

CREATE TABLE `counselor_portal` (
  `counselor_id` int(11) NOT NULL,
  `Cemail` varchar(255) NOT NULL,
  `Cpassword` varchar(255) NOT NULL,
  `status` int(255) NOT NULL,
  `reset_token` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `counselor_portal`
--

INSERT INTO `counselor_portal` (`counselor_id`, `Cemail`, `Cpassword`, `status`, `reset_token`) VALUES
(16, 'jeje@phinmaed.com', '$2b$12$wba9P3BDjEoijJvp/JqmGuDP1Cea7053B2QcvHOqmZ4O2eyBfvaxu', 1, ''),
(17, 'ben@phinmaed.com', '$2b$12$ZbVyn1WybZBnLTq6Dddl5uAT9VEGCep.HLCI3dn/Sau.48YrGU652', 1, ''),
(18, 'grace@phinmaed.com', '$2b$12$8V8GmqIhGgwGQk2fHJy8QO7BfN5kdkZKmO9HIhlTUIdLnFEcIK1si', 0, ''),
(21, 'karen@phinmaed.com', '$2b$12$9QL3mrllTjpNMK2lO2UQ.u91fQ6OFrbcu3WUfYSeCryYKe41B6V0K', 0, ''),
(22, 'kaka@phinmaed.com', '$2b$12$.mmevST3mXpxpj1Zft1dEeB0i6QINfhcN6/qVONe.7opKXetBpwL2', 0, ''),
(23, 'jema@phinmaed.com', '$2b$12$0fd6.qJUb7V82XDa5GRwGOS9LUlFfBOOr/uHSSRjCjiXu4KDRFdRm', 0, ''),
(25, 'jema@phinmaed.com', '$2b$12$nQwLcUHKhmudgiifP4L2pupAQmskItN7Ydg91kREnSL0237tSIMxq', 0, ''),
(26, 'jemima@phinmaed.com', '$2b$12$boMl1IcrlOjn4eh0i534I.S4WeyJ9ZFPn9yrwch3oSHzlTnvkhO0i', 0, ''),
(28, 'je@phinmaed.com', '$2b$12$ikELUNgTQIxP9Grq0etle.SmKb1BK51vvxc3x7fJiR5kAggqQbUqy', 0, ''),
(33, 'tin123@phinmaed.com', '$2b$12$WMgP8Jnbn051RqspZwfmdePIsZcXM8LNr/EXrRzSrtbX64N1vg0ee', 0, ''),
(35, 'jega.mariano.ui@phinmaed.com', '$2b$12$ITCZhgrK8MMr1Ci5JcHJ0uu/udCzg/V/OU3zMNJmWMifXLWjJnU3y', 1, 'U8AT7fJm0vf_QO9tyHVmHA');

-- --------------------------------------------------------

--
-- Table structure for table `session_record`
--

CREATE TABLE `session_record` (
  `record_id` int(11) NOT NULL,
  `session_email` varchar(255) NOT NULL,
  `set_date` varchar(255) DEFAULT NULL,
  `set_time` varchar(255) NOT NULL,
  `remarks` varchar(1500) NOT NULL,
  `student_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `session_record`
--

INSERT INTO `session_record` (`record_id`, `session_email`, `set_date`, `set_time`, `remarks`, `student_name`) VALUES
(39, 'kypa.pama.ui@phinmaed.com', 'April 17, 2024', '01:00:00', '', ''),
(40, 'kypa.pama.ui@phinmaed.com', 'April 25, 2024', '01:07 PM', '', ''),
(41, 'kypa.pama.ui@phinmaed.com', 'April 22, 2024', '01:00 PM', '', ''),
(42, 'kypa.pama.ui@phinmaed.com', 'July 13, 2024', '11:30 PM', '', ''),
(43, 'kypa.pama.ui@phinmaed.com', 'May 21, 2024', '11:35 PM', '', ''),
(44, 'karen@phinmaed.com', 'March 23, 2024', '09:30 AM', '', ''),
(45, 'kypa.pama.ui@phinmaed.com', 'March 23, 2024', '09:30 AM', '', ''),
(46, 'kypa.pama.ui@phinmaed.com', 'March 25, 2024', '12:00 PM', '', ''),
(47, 'kypa.pama.ui@phinmaed.com', 'March 25, 2024', '10:00 AM', '', ''),
(48, 'kypa.pama.ui@phinmaed.com', 'March 25, 2024', '10:00 AM', '', ''),
(49, 'kypa.pama.ui@phinmaed.com', 'March 25, 2024', '10:00 AM', '', ''),
(50, 'kypa.pama.ui@phinmaed.com', 'March 25, 2024', '10:00 AM', '', ''),
(51, 'kypa.pama.ui@phinmaed.com', 'March 25, 2024', '10:00 AM', '', ''),
(52, 'karen@phinmaed.com', 'March 22, 2024', '03:00 PM', '', ''),
(53, 'kyle@phinmaed.com', 'July 09, 2024', '03:00 PM', '', ''),
(54, 'kyle@phinmaed.com', 'July 09, 2024', '03:00 PM', '', ''),
(55, 'kypa.pama.ui@phinmaed.com', 'March 06, 2024', '01:32 PM', '', ''),
(56, 'kypa.pama.ui@phinmaed.com', 'March 06, 2024', '01:32 PM', '', ''),
(57, 'kypa.pama.ui@phinmaed.com', 'March 06, 2024', '01:32 PM', '', ''),
(58, 'kyle@phinmaed.com', 'March 08, 2024', '01:35 PM', '', ''),
(59, 'kyle@phinmaed.com', 'March 08, 2024', '01:35 PM', '', ''),
(60, 'karen@phinmaed.com', 'March 23, 2024', '06:46 AM', '', ''),
(61, 'karen@phinmaed.com', 'April 25, 2024', '06:30 PM', '', ''),
(62, 'kypa.pama.ui@phinmaed.com', 'March 08, 2024', '08:26 AM', '', ''),
(63, 'kypa.pama.ui@phinmaed.com', 'March 14, 2024', '08:41 AM', '', ''),
(64, 'karen@phinmaed.com', 'March 12, 2024', '12:26 AM', '', ''),
(65, 'kyle@phinmaed.com', 'March 12, 2024', '09:29 PM', '', ''),
(66, 'kypa.pama.ui@phinmaed.com', 'March 29, 2024', '09:35 AM', '', ''),
(67, 'mapo.tabarnero.ui@phinmaed.com', 'March 25, 2024', '08:00 AM', '', ''),
(68, 'karen@phinmaed.com', 'March 30, 2024', '10:00 AM', '', ''),
(69, 'stpa.sapangila.ui@phinmaed.com', 'April 01, 2024', '08:00 AM', 'please work', ''),
(70, 'kyle@phinmaed.com', 'April 04, 2024', '12:00 PM', 'tired na', ''),
(71, 'stpa.sapangila.ui@phinmaed.com', 'March 29, 2024', '05:00 AM', 'Should sleep na', ''),
(72, 'kypa.pama.ui@phinmaed.com', 'March 30, 2024', '04:00 PM', '', 'kyle'),
(73, 'kypa.pama.ui@phinmaed.com', 'March 31, 2024', '03:00 PM', '', 'kyle'),
(74, 'stpa.sapangila.ui@phinmaed.com', 'March 31, 2024', '02:00 PM', 'working?', 'Steffany'),
(75, 'kypa.pama.ui@phinmaed.com', 'March 31, 2024', '02:00 PM', 'tired', 'kyle'),
(76, 'kypa.pama.ui@phinmaed.com', 'March 31, 2024', '07:00 AM', 'rest\r\n', 'kyle'),
(77, 'stpa.sapangila.ui@phinmaed.com', 'March 31, 2024', '07:30 AM', 'almost', 'Steffany'),
(78, 'stpa.sapangila.ui@phinmaed.com', 'March 31, 2024', '04:00 PM', '', 'Steffany'),
(79, 'stpa.sapangila.ui@phinmaed.com', 'March 31, 2024', '06:00 PM', '', 'Steffany'),
(80, 'stpa.sapangila.ui@phinmaed.com', 'March 31, 2024', '07:00 PM', '', 'Steffany'),
(81, 'frpa.pama.ui@phinmaed.com', 'March 31, 2024', '10:00 PM', 'Tapos na', 'francis'),
(82, 'frpa.pama.ui@phinmaed.com', 'March 31, 2024', '10:35 PM', '', 'francis'),
(83, 'frpa.pama.ui@phinmaed.com', 'April 01, 2024', '01:00 AM', '', 'francis'),
(84, 'frpa.pama.ui@phinmaed.com', 'April 01, 2024', '01:00 AM', '', 'francis');

-- --------------------------------------------------------

--
-- Table structure for table `student_form`
--

CREATE TABLE `student_form` (
  `form_id` int(11) NOT NULL,
  `student_id` int(11) DEFAULT NULL,
  `fcomment` varchar(255) DEFAULT NULL,
  `fday` int(11) DEFAULT NULL,
  `ftime` varchar(255) DEFAULT NULL,
  `fmonth` int(11) DEFAULT NULL,
  `fyear` int(11) DEFAULT NULL,
  `dep_result` varchar(255) DEFAULT NULL,
  `anx_result` varchar(255) DEFAULT NULL,
  `stress_result` varchar(255) DEFAULT NULL,
  `dep_score` int(11) DEFAULT NULL,
  `anx_score` int(11) DEFAULT NULL,
  `stress_score` int(11) DEFAULT NULL,
  `Rid` varchar(255) NOT NULL,
  `RRid` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student_form`
--

INSERT INTO `student_form` (`form_id`, `student_id`, `fcomment`, `fday`, `ftime`, `fmonth`, `fyear`, `dep_result`, `anx_result`, `stress_result`, `dep_score`, `anx_score`, `stress_score`, `Rid`, `RRid`) VALUES
(11, NULL, 'ok', 8, '03:43 AM', 3, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 40, 30, 34, '2', ''),
(12, NULL, 'okay lang si ben Ka', 8, '03:46 AM', 3, 2024, 'Severe', 'Extremely Severe', 'Severe', 24, 26, 28, '2', ''),
(13, NULL, 'gwenchana', 8, '03:03 PM', 3, 2024, 'Moderate', 'Moderate', 'Normal', 14, 14, 14, '1', ''),
(14, NULL, 'ako nga pala si Jemima, nakatira sa molo plaza. Hinihiling ko na sana ay maging masigla ako, hindi man ngayon bukas siguro.', 9, '11:38 AM', 3, 2024, 'Severe', 'Moderate', 'Moderate', 22, 14, 20, '1', ''),
(15, 1, 'oks langs', 11, '01:01 AM', 3, 2024, 'Severe', 'Extremely Severe', 'Severe', 26, 26, 28, '', ''),
(16, 2, 'k', 11, '01:25 AM', 3, 2024, 'Moderate', 'Extremely Severe', 'Mild', 18, 28, 16, '', ''),
(17, 2, 'Ma\'am I really need your advice huhu', 17, '01:32 AM', 3, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 42, 42, 42, '', ''),
(18, 1, 'Liwat hehe', 17, '01:35 AM', 3, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 42, 42, 42, '', ''),
(19, 1, 'Liwat liwat kay error', 17, '01:38 AM', 3, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 42, 42, 42, '', ''),
(20, 1, 'Okay lang man, ari ga face ko errors', 18, '02:24 PM', 3, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 36, 32, 34, '', ''),
(22, 2, 'gwenchana', 19, '04:34 PM', 3, 2024, 'Normal', 'Normal', 'Normal', 2, 6, 6, '', ''),
(23, 1, 'I want to die, huhu', 19, '05:35 PM', 3, 2024, 'Moderate', 'Extremely Severe', 'Normal', 14, 26, 12, '', ''),
(24, 1, 'malalaman ko yan sa result', 19, '11:40 PM', 3, 2024, 'Moderate', 'Extremely Severe', 'Moderate', 18, 22, 20, '1', ''),
(25, 2, 'Damo errors po', 20, '12:47 AM', 3, 2024, 'Moderate', 'Severe', 'Mild', 16, 16, 16, '2', ''),
(26, 1, 'Makapasa lang ko sa capstone Ma\'am, okay na ako', 20, '01:01 AM', 3, 2024, 'Moderate', 'Moderate', 'Normal', 14, 12, 6, '1', ''),
(27, 2, 'Mag work kana please, no more errors na please', 20, '01:07 AM', 3, 2024, 'Severe', 'Extremely Severe', 'Mild', 22, 26, 16, '2', ''),
(28, 1, 'Sana mag work, yun lang ang hinihiling ko ngayong 1:19 am', 20, '01:19 AM', 3, 2024, 'Severe', 'Extremely Severe', 'Normal', 22, 24, 10, '1', ''),
(29, 1, 'Error', 20, '02:25 AM', 3, 2024, 'Severe', 'Extremely Severe', 'Mild', 22, 24, 18, '1', ''),
(30, 1, 'hehe ', 20, '03:06 AM', 3, 2024, 'Moderate', 'Severe', 'Moderate', 20, 18, 20, '1', '1'),
(31, 1, 'Sleep na akoo', 20, '03:09 AM', 3, 2024, 'Moderate', 'Severe', 'Moderate', 20, 18, 20, '1', '1'),
(32, 2, 'Ay ilam', 20, '02:55 PM', 3, 2024, 'Mild', 'Severe', 'Mild', 10, 16, 18, '2', '2'),
(40, 3, 'not gwenchana', 20, '11:50 PM', 3, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 40, 38, 40, '3', '3'),
(41, 3, 'hehe', 21, '12:24 AM', 3, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 42, 38, 42, '3', '3'),
(42, 4, 'Hoping for the best', 21, '03:05 AM', 3, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 30, 36, 38, '', ''),
(43, 1, 'Ga work na ang code Ma\'am', 21, '03:11 PM', 3, 2024, 'Extremely Severe', 'Extremely Severe', 'Severe', 30, 36, 30, '', ''),
(44, 1, 'Okay lang', 22, '03:48 PM', 3, 2024, 'Severe', 'Extremely Severe', 'Severe', 22, 30, 28, '', ''),
(45, 5, 'Idk', 23, '01:31 PM', 3, 2024, 'Mild', 'Moderate', 'Severe', 12, 14, 28, '', ''),
(46, 3, 'keri', 27, '12:20 AM', 3, 2024, 'Moderate', 'Moderate', 'Normal', 14, 14, 14, '', ''),
(47, 6, 'Daijoubu', 28, '10:44 PM', 3, 2024, 'Moderate', 'Moderate', 'Normal', 14, 14, 14, '', ''),
(48, 6, '', 29, '01:55 AM', 3, 2024, 'Moderate', 'Moderate', 'Normal', 14, 14, 14, '', ''),
(49, 6, '', 29, '04:26 AM', 3, 2024, 'Normal', 'Normal', 'Normal', 0, 0, 0, '', ''),
(50, 6, 'Stress', 29, '04:27 AM', 3, 2024, 'Severe', 'Normal', 'Normal', 30, 0, 0, '', ''),
(52, 6, 'Anxious', 30, '12:06 AM', 3, 2024, 'Normal', 'Severe', 'Normal', 0, 30, 0, '', ''),
(53, 6, 'Stressed', 30, '12:07 AM', 3, 2024, 'Normal', 'Normal', 'Severe', 0, 0, 30, '', ''),
(54, 6, '', 30, '12:16 AM', 3, 2024, 'Severe', 'Severe', 'Severe', 30, 30, 30, '', ''),
(55, 6, '', 30, '12:16 AM', 3, 2024, 'Severe', 'Severe', 'Severe', 30, 30, 30, '', ''),
(56, 6, '', 30, '12:16 AM', 3, 2024, 'Severe', 'Severe', 'Severe', 30, 30, 30, '', ''),
(57, 6, '', 30, '12:24 AM', 3, 2024, 'Severe', 'Severe', 'Severe', 30, 30, 30, '', ''),
(58, 6, '', 30, '12:25 AM', 3, 2024, 'Severe', 'Severe', 'Severe', 30, 30, 30, '', ''),
(59, 6, '', 30, '12:26 AM', 3, 2024, 'Severe', 'Severe', 'Severe', 30, 30, 30, '', ''),
(60, 6, '', 30, '12:26 AM', 3, 2024, 'Severe', 'Severe', 'Severe', 30, 30, 30, '', ''),
(61, 6, '', 30, '12:27 AM', 3, 2024, 'Severe', 'Severe', 'Severe', 30, 30, 30, '', ''),
(62, 6, '', 30, '12:27 AM', 3, 2024, 'Severe', 'Severe', 'Severe', 30, 30, 30, '', ''),
(63, 6, '', 30, '12:27 AM', 3, 2024, 'Severe', 'Severe', 'Severe', 30, 30, 30, '', ''),
(64, 6, '', 30, '01:08 AM', 3, 2024, 'Severe', 'Severe', 'Severe', 30, 30, 30, '', ''),
(65, 6, '', 30, '02:37 PM', 3, 2024, 'Severe', 'Severe', 'Severe', 30, 30, 30, '', ''),
(66, 6, 'Almost', 30, '09:11 PM', 3, 2024, 'Severe', 'Severe', 'Severe', 30, 30, 30, '', ''),
(67, 6, 'Almost', 30, '09:12 PM', 3, 2024, 'Severe', 'Severe', 'Severe', 30, 30, 30, '', ''),
(68, 6, 'Almost', 30, '09:12 PM', 3, 2024, 'Severe', 'Severe', 'Severe', 30, 30, 30, '', ''),
(69, 6, 'Almost', 30, '09:12 PM', 3, 2024, 'Severe', 'Severe', 'Severe', 30, 30, 30, '', ''),
(70, 6, 'Almost', 30, '09:12 PM', 3, 2024, 'Severe', 'Severe', 'Severe', 30, 30, 30, '', ''),
(71, 3, 'Gwencha²', 31, '07:17 PM', 3, 2024, 'Mild', 'Mild', 'Mild', 10, 10, 10, '', ''),
(72, 3, 'Gwencha²', 31, '07:19 PM', 3, 2024, 'Mild', 'Mild', 'Mild', 10, 10, 10, '', ''),
(73, 7, 'nice', 31, '09:13 PM', 3, 2024, 'Mild', 'Mild', 'Moderate', 14, 14, 16, '', '');

-- --------------------------------------------------------

--
-- Table structure for table `student_portal`
--

CREATE TABLE `student_portal` (
  `student_id` int(11) NOT NULL,
  `Sid_number` varchar(255) DEFAULT NULL,
  `Semail` varchar(255) DEFAULT NULL,
  `Sfirst_name` varchar(255) DEFAULT NULL,
  `Slast_name` varchar(255) DEFAULT NULL,
  `Scourse` varchar(255) DEFAULT NULL,
  `Spassword` varchar(255) DEFAULT NULL,
  `reset_token` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student_portal`
--

INSERT INTO `student_portal` (`student_id`, `Sid_number`, `Semail`, `Sfirst_name`, `Slast_name`, `Scourse`, `Spassword`, `reset_token`) VALUES
(1, '04-2122-032201', 'jega.mariano.ui@phinmaed.com', 'Jemima', 'Mariano', 'BSIT', '$2b$12$wcR4ZgsrjxTjWF5gZOlE3eCY0uq/8vHP4LobrP8JZKfJvC36W.rb6', ''),
(2, '09-3464-346424', 'karen@phinmaed.com', 'Karen', 'Gaytano', 'BSCE', '$2b$12$Oo/zInUrf8/51WRp7qho7ObFEqdmfVtHYEoOugsbhgSIZ.28qp3SO', ''),
(3, '09-2122-032201', 'kyle@phinmaed.com', 'kyle', 'pama', 'BSAIS', '$2b$12$ZZK4fbOIi8e/NWysasqen.VqaaSUDz.1I7M5OTq7FwrvD1SVAFr5a', ''),
(4, '04-2122-032201', 'kypa.pama.ui@phinmaed.com', 'kyle', 'pama', 'BSIT', '$2b$12$Z.6voA4gf1innVURpfHTGu1BWEQNKnTrRkDtkMOzKzek5WQ1QC99W', ''),
(5, '04-1920-00805', 'mapo.tabarnero.ui@phinmaed.com', 'Mary Grace', 'Tabarnero', 'BSIT', '$2b$12$fUR1Txw0mMif3lZwIIqel.EWrncETyKhZsg.a5aRnhOnPVX3b55Ce', ''),
(6, '04-2122-032419', 'stpa.sapangila.ui@phinmaed.com', 'Steffany', 'Sapangila', 'BSHRM', '$2b$12$watiP29cw.lQr8ihr06XlOrIfObupKhH0/P4ceCX9WpV9YKAUMM8y', ''),
(7, '01-2464-80872', 'frpa.pama.ui@phinmaed.com', 'francis', 'pama', 'BSME', '$2b$12$XtQBSN3lh0z6Kwb5rdbyfuIN6QFqcocXZlEdkvLg9FmU826wzY7wu', 'rUCwh5Q5gSxy3aSjQJ4Bhg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_portal`
--
ALTER TABLE `admin_portal`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `counselor_portal`
--
ALTER TABLE `counselor_portal`
  ADD PRIMARY KEY (`counselor_id`);

--
-- Indexes for table `session_record`
--
ALTER TABLE `session_record`
  ADD PRIMARY KEY (`record_id`);

--
-- Indexes for table `student_form`
--
ALTER TABLE `student_form`
  ADD PRIMARY KEY (`form_id`),
  ADD KEY `student_id` (`student_id`);

--
-- Indexes for table `student_portal`
--
ALTER TABLE `student_portal`
  ADD PRIMARY KEY (`student_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_portal`
--
ALTER TABLE `admin_portal`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `counselor_portal`
--
ALTER TABLE `counselor_portal`
  MODIFY `counselor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `session_record`
--
ALTER TABLE `session_record`
  MODIFY `record_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=85;

--
-- AUTO_INCREMENT for table `student_form`
--
ALTER TABLE `student_form`
  MODIFY `form_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=74;

--
-- AUTO_INCREMENT for table `student_portal`
--
ALTER TABLE `student_portal`
  MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `student_form`
--
ALTER TABLE `student_form`
  ADD CONSTRAINT `student_form_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student_portal` (`student_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
