#include <stdio.h>


float inss_tax(float brute_salary)
{
	return brute_salary*0.08;
}

float brute_salary(float hour_of_work, float worked_hours)
{
	return hour_of_work*worked_hours;
}

float synd_tax(float brute_salary)
{
	return brute_salary*0.05;
}

float income_tax(float brute_salary)
{
	return brute_salary*0.11;
}

float pure_salary(float brute_salary)
{
	return brute_salary - (income_tax(brute_salary)+synd_tax(brute_salary)+inss_tax(brute_salary));
}


struct salary_elements
{
	float inss_tax;
	float brute_salary;
	float synd_tax;
	float pure_salary;
	float income_tax;
};


struct salary_elements info_salary(float hour_of_work, float worked_hours)
{
	struct salary_elements salary;
	salary.inss_tax = inss_tax(brute_salary(hour_of_work,worked_hours));
	salary.brute_salary = brute_salary(hour_of_work,worked_hours);
	salary.synd_tax = synd_tax(brute_salary(hour_of_work,worked_hours)); 
	salary.pure_salary = pure_salary(brute_salary(hour_of_work,worked_hours));
	salary.income_tax = income_tax(brute_salary(hour_of_work,worked_hours));
	return salary;
}


main()
{
	struct salary_elements salary;
	float worked_hours, hour_value;
	printf("input your work hour value--> ");
	scanf("%f", &hour_value);
	printf("input your worked hours--> ");
        scanf("%f", &worked_hours);
	salary = info_salary(hour_value,worked_hours);
	printf("\nTotal: $%.2f\n",salary.brute_salary);
        printf("Income tax: $%.2f\n", salary.income_tax);
        printf("Synd tax: $%.2f\n", salary.synd_tax);
        printf("Inss tax: $%.2f\n", salary.inss_tax);
        printf("Pure salary: $%.2f\n\n", salary.pure_salary);
	
}

