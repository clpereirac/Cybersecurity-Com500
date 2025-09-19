#!/usr/bin/env python3
"""
Simple Password Strength Checker
Educational tool for Cybersecurity COM500 course

This script evaluates password strength based on common security criteria.
Use this tool to understand password security principles.

Author: Cybersecurity COM500 Course
License: Educational Use Only
"""

import re
import sys
import getpass
from typing import Tuple, List


def check_password_strength(password: str) -> Tuple[int, List[str]]:
    """
    Evaluate password strength and return score with feedback.
    
    Args:
        password: The password to evaluate
        
    Returns:
        Tuple of (score, feedback_list)
    """
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 12:
        score += 25
        feedback.append("✓ Good length (12+ characters)")
    elif len(password) >= 8:
        score += 15
        feedback.append("⚠ Acceptable length (8+ characters), but longer is better")
    else:
        feedback.append("✗ Too short (less than 8 characters)")
    
    # Uppercase letters
    if re.search(r'[A-Z]', password):
        score += 15
        feedback.append("✓ Contains uppercase letters")
    else:
        feedback.append("✗ Missing uppercase letters")
    
    # Lowercase letters
    if re.search(r'[a-z]', password):
        score += 15
        feedback.append("✓ Contains lowercase letters")
    else:
        feedback.append("✗ Missing lowercase letters")
    
    # Numbers
    if re.search(r'\d', password):
        score += 15
        feedback.append("✓ Contains numbers")
    else:
        feedback.append("✗ Missing numbers")
    
    # Special characters
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]', password):
        score += 20
        feedback.append("✓ Contains special characters")
    else:
        feedback.append("✗ Missing special characters")
    
    # Common patterns check
    common_patterns = [
        r'123+',       # Sequential numbers
        r'abc+',       # Sequential letters
        r'password',   # Common word
        r'qwerty',     # Keyboard pattern
        r'admin',      # Common word
    ]
    
    pattern_found = False
    for pattern in common_patterns:
        if re.search(pattern, password.lower()):
            score -= 20
            feedback.append("✗ Contains common pattern or word")
            pattern_found = True
            break
    
    if not pattern_found:
        score += 10
        feedback.append("✓ No obvious patterns detected")
    
    return max(0, min(100, score)), feedback


def get_strength_rating(score: int) -> str:
    """Convert numeric score to strength rating."""
    if score >= 80:
        return "STRONG"
    elif score >= 60:
        return "MODERATE"
    elif score >= 40:
        return "WEAK"
    else:
        return "VERY WEAK"


def get_color_code(rating: str) -> str:
    """Get ANSI color code for strength rating."""
    colors = {
        "STRONG": "\033[92m",      # Green
        "MODERATE": "\033[93m",    # Yellow
        "WEAK": "\033[91m",        # Red
        "VERY WEAK": "\033[95m"    # Magenta
    }
    return colors.get(rating, "\033[0m")


def main():
    """Main function to run the password strength checker."""
    print("=" * 60)
    print("Password Strength Checker - Cybersecurity COM500")
    print("=" * 60)
    print()
    
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help']:
        print("Usage: python3 password_checker.py")
        print("This tool evaluates password strength interactively.")
        print("\nSecurity Note: Password input is hidden for security.")
        print("For educational purposes only.")
        return
    
    try:
        # Get password securely (hidden input)
        password = getpass.getpass("Enter password to check (hidden): ")
        
        if not password:
            print("No password entered. Exiting.")
            return
        
        # Evaluate password
        score, feedback = check_password_strength(password)
        rating = get_strength_rating(score)
        color = get_color_code(rating)
        
        # Display results
        print("\n" + "=" * 40)
        print("PASSWORD STRENGTH ANALYSIS")
        print("=" * 40)
        print(f"Score: {score}/100")
        print(f"Rating: {color}{rating}\033[0m")
        print("\nDetailed Feedback:")
        print("-" * 20)
        
        for item in feedback:
            print(f"  {item}")
        
        print("\n" + "=" * 40)
        print("SECURITY RECOMMENDATIONS")
        print("=" * 40)
        
        if score < 80:
            print("• Use at least 12 characters")
            print("• Include uppercase and lowercase letters")
            print("• Add numbers and special characters")
            print("• Avoid common words and patterns")
            print("• Consider using a passphrase")
            print("• Use a password manager for unique passwords")
        else:
            print("• Your password meets strong security criteria")
            print("• Consider using a password manager")
            print("• Enable two-factor authentication when available")
        
        print("\nRemember: Never reuse passwords across multiple accounts!")
        
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()