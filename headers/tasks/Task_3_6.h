#ifndef PROBABILITYTHEORY_TASK_3_6_H
#define PROBABILITYTHEORY_TASK_3_6_H

class Task_3_6
{
private:
    bool CheckIntersectionWithRectangle(double x, double y, double r, double recX, double recY);
    bool CheckNonIntersection(double x, double y, double r, double ellA, double ellB, double recX,
                              double recY, double circles[][2], int n, double stepX, double epsY);

public:
    Task_3_6();
    void Start(int numberOfCircleIterations, int numberOfPointIterations, int numberOfCircles, double r,
               double ellA, double ellB, double recX, double recY, double rB, double stepX, double epsY);
};

#endif
