def calculate_salary(basic_pay, pf_percentage, hra_percentage, da_percentage):
    # Calculate PF, HRA, and DA based on percentages provided
    pf = (pf_percentage / 100) * basic_pay
    hra = (hra_percentage / 100) * basic_pay
    da = (da_percentage / 100) * basic_pay
    
    # Calculate total salary
    total_salary = basic_pay + hra + da - pf
    
    return {
        'Basic Pay': basic_pay,
        'PF': pf,
        'HRA': hra,
        'DA': da,
        'Total Salary': total_salary
    }

# Example usage:
basic_pay = 50000  # Basic salary amount
pf_percentage = 12  # PF percentage
hra_percentage = 20  # HRA percentage
da_percentage = 10  # DA percentage

salary_details = calculate_salary(basic_pay, pf_percentage, hra_percentage, da_percentage)


