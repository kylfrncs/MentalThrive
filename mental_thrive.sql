-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306:3306
-- Generation Time: Mar 10, 2024 at 11:09 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

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
  `Cpassword` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `counselor_portal`
--

INSERT INTO `counselor_portal` (`counselor_id`, `Cemail`, `Cpassword`) VALUES
(16, 'jeje@phinmaed.com', '$2b$12$wba9P3BDjEoijJvp/JqmGuDP1Cea7053B2QcvHOqmZ4O2eyBfvaxu'),
(17, 'ben@phinmaed.com', '$2b$12$ZbVyn1WybZBnLTq6Dddl5uAT9VEGCep.HLCI3dn/Sau.48YrGU652'),
(18, 'grace@phinmaed.com', '$2b$12$8V8GmqIhGgwGQk2fHJy8QO7BfN5kdkZKmO9HIhlTUIdLnFEcIK1si'),
(21, 'karen@phinmaed.com', '$2b$12$9QL3mrllTjpNMK2lO2UQ.u91fQ6OFrbcu3WUfYSeCryYKe41B6V0K'),
(22, 'kaka@phinmaed.com', '$2b$12$.mmevST3mXpxpj1Zft1dEeB0i6QINfhcN6/qVONe.7opKXetBpwL2'),
(23, 'jema@phinmaed.com', '$2b$12$0fd6.qJUb7V82XDa5GRwGOS9LUlFfBOOr/uHSSRjCjiXu4KDRFdRm'),
(25, 'jema@phinmaed.com', '$2b$12$nQwLcUHKhmudgiifP4L2pupAQmskItN7Ydg91kREnSL0237tSIMxq'),
(26, 'jemima@phinmaed.com', '$2b$12$boMl1IcrlOjn4eh0i534I.S4WeyJ9ZFPn9yrwch3oSHzlTnvkhO0i'),
(27, 'mima@phinmaed.com', '$2b$12$TiZuKYr0GGFJKAOGCaz1EOYMLeGpIQbrum6oe54gEPrRDuHG9TOtu'),
(28, 'je@phinmaed.com', '$2b$12$ikELUNgTQIxP9Grq0etle.SmKb1BK51vvxc3x7fJiR5kAggqQbUqy');

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
  `Rid` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student_form`
--

INSERT INTO `student_form` (`form_id`, `student_id`, `fcomment`, `fday`, `ftime`, `fmonth`, `fyear`, `dep_result`, `anx_result`, `stress_result`, `dep_score`, `anx_score`, `stress_score`, `Rid`) VALUES
(1, NULL, 'Okay lang Ma\'am kailangan lang ng advice ni Enrique Gil \'_\'', 7, '12:12:00', 3, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 32, 34, 34, '0'),
(2, NULL, 'This is my second day at akala ko mawawala na yung nararamdaman ko sa kaniya.', 7, '12:26 AM', 3, 2024, 'Moderate', 'Extremely Severe', 'Moderate', 18, 32, 24, '0'),
(3, NULL, 'Kailangan ko po ng advice niyo Ma\'am kasi ilang araw nag-iisip kung magpapatuloy pa ba ako sa pag-aaral o hindi na.', 7, '12:31 AM', 3, 2024, 'Severe', 'Extremely Severe', 'Moderate', 26, 32, 20, '0'),
(4, NULL, 'huhuhu', 7, '02:11 AM', 3, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 34, 36, 34, '0'),
(5, NULL, 'Hello I need some piece of advice.', 7, '02:19 AM', 3, 2024, 'Extremely Severe', 'Extremely Severe', 'Severe', 34, 32, 26, '0'),
(6, NULL, 'Hindi ko na po alam ang gagawin ko.', 7, '02:52 AM', 3, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 38, 30, 36, '0'),
(7, NULL, 'Okay lang kailangan ko ng skin care.', 8, '02:53 AM', 3, 2024, 'Extremely Severe', 'Extremely Severe', 'Severe', 34, 36, 28, '0'),
(8, NULL, 'Okay langsz', 8, '03:36 AM', 3, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 30, 28, 34, '0'),
(9, NULL, 'Okay langsz', 8, '03:37 AM', 3, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 30, 28, 34, '0'),
(10, NULL, 'Okay langsz', 8, '03:38 AM', 3, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 30, 28, 34, '0'),
(11, NULL, 'ok', 8, '03:43 AM', 3, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 40, 30, 34, '2'),
(12, NULL, 'okay lang si ben Ka', 8, '03:46 AM', 3, 2024, 'Severe', 'Extremely Severe', 'Severe', 24, 26, 28, '2'),
(13, NULL, 'gwenchana', 8, '03:03 PM', 3, 2024, 'Moderate', 'Moderate', 'Normal', 14, 14, 14, '1'),
(14, NULL, 'ako nga pala si Jemima, nakatira sa molo plaza. Hinihiling ko na sana ay maging masigla ako, hindi man ngayon bukas siguro.', 9, '11:38 AM', 3, 2024, 'Severe', 'Moderate', 'Moderate', 22, 14, 20, '1');

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
  `Spassword` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student_portal`
--

INSERT INTO `student_portal` (`student_id`, `Sid_number`, `Semail`, `Sfirst_name`, `Slast_name`, `Scourse`, `Spassword`) VALUES
(1, '04-2122-032201', 'mima@phinmaed.com', 'Jemima', 'Mariano', 'BSIT', '$2b$12$wcR4ZgsrjxTjWF5gZOlE3eCY0uq/8vHP4LobrP8JZKfJvC36W.rb6'),
(2, '09-3464-346424', 'karen@phinmaed.com', 'Karen', 'Gaytano', 'BSCE', '$2b$12$Oo/zInUrf8/51WRp7qho7ObFEqdmfVtHYEoOugsbhgSIZ.28qp3SO'),
(3, '09-2122-032201', 'kyle@phinmaed.com', 'kyle', 'pama', 'BSAIS', '$2b$12$ZZK4fbOIi8e/NWysasqen.VqaaSUDz.1I7M5OTq7FwrvD1SVAFr5a');

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
  MODIFY `counselor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `student_form`
--
ALTER TABLE `student_form`
  MODIFY `form_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `student_portal`
--
ALTER TABLE `student_portal`
  MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

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
