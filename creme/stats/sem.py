from . import var


class SEM(var.Var):
    """Running standard error of the mean using Welford's algorithm.

    Parameters:
        ddof (int): Delta Degrees of Freedom. The divisor used in calculations is $n$ - ddof,
            where $n$ represents the number of seen elements.

    Attributes:
        n (int): Number of observations.

    Example:

        ::

            >>> import creme.stats

            >>> X = [3, 5, 4, 7, 10, 12]

            >>> sem = creme.stats.SEM()
            >>> for x in X:
            ...     print(sem.update(x).get())
            0.0
            1.0
            0.577350...
            0.853912...
            1.240967...
            1.447219...

    References:

        1. `Welford's online algorithm <https://www.wikiwand.com/en/Algorithms_for_calculating_variance#/Welford's_Online_algorithm>`_

    """

    @property
    def name(self):
        return 'sem'

    def get(self):
        return (super().get() / self.mean.n) ** 0.5


class RollingSEM(var.RollingVar):
    """Running standard error of the mean over a window.

    Parameters:
        window_size (int): Size of the rolling window.
        ddof (int): Delta Degrees of Freedom for the variance.

    Example:

        ::
            >>> import creme

            >>> X = [1, 4, 2, -4, -8, 0]

            >>> rolling_sem = creme.stats.RollingSEM(ddof=1, window_size=2)
            >>> for x in X:
            ...     print(rolling_sem.update(x).get())
            0.0
            1.5
            1.0
            3.0
            2.0
            4.0

            >>> rolling_sem = creme.stats.RollingSEM(ddof=1, window_size=3)
            >>> for x in X:
            ...     print(rolling_sem.update(x).get())
            0.0
            1.5
            0.881917...
            2.403700...
            2.905932...
            2.309401...

    """

    @property
    def name(self):
        return f'rolling_{self.size}_sem'

    def get(self):
        return (super().get() / len(self.rolling_mean)) ** 0.5
